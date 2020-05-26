import uuid

from PyQt5 import QtSql, QtCore


def create():
    query = QtSql.QSqlQuery()
    query.exec_("create table if not exists flight("
                "id varchar(20) primary key,"
                "name varchar(20),"
                "start varchar(20),"
                "end varchar(20))")

    query.exec_("create table if not exists seat("
                "id varchar(20),"
                "grade varchar(20),"
                "count int,"
                "remain int,"
                "price float,"
                "primary key (id,grade))")

    query.exec_("create table if not exists client("
                "id varchar(20) primary key,"
                "name varchar(20),"
                "phone varchar(20))")

    query.exec_("create table if not exists record("
                "id varchar(32) primary key,"
                "clientname varchar(20),"
                "clientid varchar(20),"
                "flightid varchar(20),"
                "flightname varchar(20),"
                "start varchar(20),"
                "end varchar(20),"
                "grade varchar(20),"
                "price float)")
    print('创建表成功')


def create_flight(id, name, start, end):
    query = QtSql.QSqlQuery()
    query.prepare('insert into flight values (?, ?, ?, ?)')
    query.addBindValue(id)
    query.addBindValue(name)
    query.addBindValue(start)
    query.addBindValue(end)

    if not query.exec_():
        return query.lastError().text()
    else:
        return 'success'


def create_seat(id, grade, count, remain, price):
    if count <= 0:
        return 'success'

    query = QtSql.QSqlQuery()
    query.prepare('insert into seat values (?, ?, ?, ?, ?)')
    query.addBindValue(id)
    query.addBindValue(grade)
    query.addBindValue(count)
    query.addBindValue(remain)
    query.addBindValue(price)

    if not query.exec_():
        return query.lastError().text()
    else:
        return 'success'


def create_client(name, id, phone):
    query = QtSql.QSqlQuery()
    query.prepare('insert into client values (?, ?, ?)')
    query.addBindValue(id)
    query.addBindValue(name)
    query.addBindValue(phone)

    if not query.exec_():
        return query.lastError().text()
    else:
        return 'success'


def modify_price(flight_id, grade, price):
    query = QtSql.QSqlQuery()
    query.prepare('update seat set price = ? where id = ? and grade = ?')
    query.addBindValue(price)
    query.addBindValue(flight_id)
    query.addBindValue(grade)
    if not query.exec_():
        return query.lastError().text()
    else:
        return 'success'


def is_ticket_empty(flight_id, grade):
    query = QtSql.QSqlQuery()
    query.prepare('select remain from seat where id = ? and grade = ?')
    query.addBindValue(flight_id)
    query.addBindValue(grade)

    if not query.exec_():
        return query.lastError().text()
    else:
        while query.next():
            remain = int(query.value(0))
            if remain > 0:
                return False
            else:
                return True
        return False


def buy_ticket(client_id, flight_id, flight_name, start, end, grade):
    record_id = str(uuid.uuid1()).replace('-', '')

    query = QtSql.QSqlQuery()
    query.prepare('insert into record (id, clientid, flightid, flightname, start, end, grade) values (?,?,?,?,?,?,?)')
    query.addBindValue(record_id)
    query.addBindValue(client_id)
    query.addBindValue(flight_id)
    query.addBindValue(flight_name)
    query.addBindValue(start)
    query.addBindValue(end)
    query.addBindValue(grade)

    if not query.exec_():
        return query.lastError().text()

    query.prepare('update record set price = ('
                  'select price from seat where id = ? and grade = ?) '
                  'where id = ?')
    query.addBindValue(flight_id)
    query.addBindValue(grade)
    query.addBindValue(record_id)

    if not query.exec_():
        return query.lastError().text()

    query = QtSql.QSqlQuery()

    query.prepare('update seat set remain = remain - 1 where id = ? and grade = ?')
    query.addBindValue(flight_id)
    query.addBindValue(grade)

    if not query.exec_():
        return query.lastError().text()

    return 'success'


def query_flight(flight_id, flight_name, start, end):
    condition = ""
    if flight_id:
        condition += "id = '" + flight_id + "' "
    if flight_name:
        condition += "name = '" + flight_name + "' "
    if start:
        condition += " start = '" + start + "' "
    if end:
        condition += " end = '" + end + "' "
    if condition:
        condition = 'where ' + condition
    # 实例化一个可编辑数据模型
    model = QtSql.QSqlQueryModel()
    model.setQuery('select f.id, name, start, end, grade, price, count, remain '
                   'from flight as f inner join seat as s on f.id = s.id '
                   + condition +
                   'order by f.id ')
    # 设置表格头
    model.setHeaderData(0, QtCore.Qt.Horizontal, '航班编号')
    model.setHeaderData(1, QtCore.Qt.Horizontal, '航班名称')
    model.setHeaderData(2, QtCore.Qt.Horizontal, '起始地')
    model.setHeaderData(3, QtCore.Qt.Horizontal, '目的地')
    model.setHeaderData(4, QtCore.Qt.Horizontal, '舱位等级')
    model.setHeaderData(5, QtCore.Qt.Horizontal, '价格')
    model.setHeaderData(6, QtCore.Qt.Horizontal, '舱位总数')
    model.setHeaderData(7, QtCore.Qt.Horizontal, '舱位剩余')
    return model


def query_seat(flight_id, grade):
    query = QtSql.QSqlQuery()
    query.prepare('select price, count from seat where id = ? and grade = ?')
    query.addBindValue(flight_id)
    query.addBindValue(grade)
    if not query.exec_():
        return 'error', query.lastError().text(), None
    else:
        while query.next():
            price = query.value(0)
            count = query.value(1)
            return 'success', price, count
    return 'success', None, 0


def query_client(id):
    query = QtSql.QSqlQuery()
    query.prepare('select * from client where id = ?')
    query.addBindValue(id)
    if not query.exec_():
        return 'error', query.lastError().text()
    else:
        while query.next():
            id = query.value(0)
            name = query.value(1)
            phone = query.value(2)
            return 'success', (id, name, phone)
    return 'success', None


def query_all_client():
    model = QtSql.QSqlQueryModel()
    model.setQuery('select name, id, phone from client')
    # 设置表格头
    model.setHeaderData(0, QtCore.Qt.Horizontal, '姓名')
    model.setHeaderData(1, QtCore.Qt.Horizontal, '证件号')
    model.setHeaderData(2, QtCore.Qt.Horizontal, '电话')
    return model


def query_record(client_id):
    model = QtSql.QSqlQueryModel()
    model.setQuery("select id, flightid, flightname, start, end, grade, price "
                   "from record "
                   "where clientid = '" + client_id + "'")

    model.setHeaderData(0, QtCore.Qt.Horizontal, '流水号')
    model.setHeaderData(1, QtCore.Qt.Horizontal, '航班编号')
    model.setHeaderData(2, QtCore.Qt.Horizontal, '航班名称')
    model.setHeaderData(3, QtCore.Qt.Horizontal, '起始地')
    model.setHeaderData(4, QtCore.Qt.Horizontal, '目的地')
    model.setHeaderData(5, QtCore.Qt.Horizontal, '舱位等级')
    model.setHeaderData(6, QtCore.Qt.Horizontal, '票价')
    return model
