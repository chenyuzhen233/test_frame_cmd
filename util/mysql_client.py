# coding=utf-8
import sys
from config import config
from log import logger
try:
    import pymysql
except ImportError:
    print("请先安装pymysql库！")


class MySQLClient(object):
    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.connection = self.connected_db()
        self.cursor = self.connection.cursor()

    def connected_db(self):
        try:
            connection = pymysql.connect(host=self.host,
                                         port=self.port,
                                         user=self.user,
                                         password=self.password,
                                         db=self.db,
                                         charset=self.charset,
                                         cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print('数据库连接失败！')
            print(repr(e))
            sys.exit()
        return connection

    def disconnected_db(self):
        self.db.close()

    def select(self, table, where, search):
        '''
        :param table: 需要查询的表名  eg: Account  
        :param where: 条件语句 eg: name = 'XiaoMing' and sex = '0'
        :param search: 需要查询的字段 eg： ['accountId', 'address']
        :return: eg: [{u'accountId': u'test1', u'address': 1},
                      {u'accountId': u'test2', u'address': 2}]
        '''  
        sql_search = ','.join(search)  
        sql = 'select %s from %s where %s;' % (sql_search, table, where)  
        try:  
            self.cursor.execute(sql)  
        except pymysql.err.ProgrammingError as e:
            logger.warn('SQL 语句编写异常，请检查参数是否正确')
            logger.warn(repr(e))
            logger.warn('sql:%s' % sql)
            sys.exit()  
        result = self.cursor.fetchall()
        self.connection.commit()
        return result


mysql_client = MySQLClient(host=config.get('database', 'host'),
                           port=int(config.get('database', 'port')),
                           user=config.get('database', 'user'),
                           password=config.get('database', 'password'),
                           db=config.get('database', 'db'),
                           charset=config.get('database', 'charset'))

if __name__ == '__main__':
    db = mysql_client
    result = db.select(table="user", where="id=1",search=['name','create_time'])
    print result