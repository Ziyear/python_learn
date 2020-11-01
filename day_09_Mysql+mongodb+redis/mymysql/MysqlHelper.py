from pymysql import *


class MysqlHelper(object):
    """mysql 工具"""

    def __init__(self, host, port, db, user, password, charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.charset = charset

    def open(self):
        self.conn = Connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db,
                            charset=self.charset)
        self.cursor = self.conn.cursor(cursors.DictCursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def update(self, sql, params=()):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            print("OS error: {0}".format(e))
        finally:
            self.close()

    def execute(self, sql, params=()):
        try:
            self.open()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.conn.commit()
            return result
        except Exception as e:
            print("OS error: {0}".format(e))
        finally:
            self.close()
