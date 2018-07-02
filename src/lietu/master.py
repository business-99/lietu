import pymysql
try:
    import cx_Oracle
except ImportError:
    print('注意：不能导入oracle组件...请检查客户端是否安装成功...!')

class Canine(object):
    sql = ""

    def __init__(self, obj=None):
        self.obj = obj

    def trace(self, param):
        assert self.sql, 'sql is require!'
        conn = None
        try:
            conn = self.get_db_conn()
            cursor = conn.cursor()
            cursor.execute(self.sql.format(param))
            rabbits = cursor.fetchall()
            if len(rabbits) == 0:
                rabbits = "参数无效，查无信息！"
        finally:
            if conn:
                conn.close()
        return rabbits

    def get_db_conn(self):
        database = self.obj.databases.first()
        if not database:
            raise ValueError('the scripts does not state a database!')
        if database.db_type == 'mysql':
            db_info = {
                'host': database.db_host,
                'port': int(database.db_port),
                'database': database.db_name,
                'user': database.db_user,
                'password': database.db_pwd,
            }
            conn = pymysql.connect(**db_info)
        elif database.db_type == 'oracle':
            db_info = '{}/{}@{}:{}/{}'.format(database.db_user, database.db_pwd,
                                              database.db_host, database.db_port,
                                              database.db_name)
            conn = cx_Oracle.connect(db_info)
        else:
            raise ValueError('the script do not support {} database!'.format(database.db_type))
        return conn
