import MySQLdb



class DBModel:
    hostname = "127.0.0.1"
    username = "root"
    password = "root"
    database = "custom_predict_house_system"

    def __init__(self):
        self.open_db_connection()


    def select_db_data(self, table_name, where_filter):
        query = "select label from {} where value = {} limit 1".format(table_name, where_filter)

        self.cursor_obj.execute(query)

        row = self.cursor_obj.fetchone()

        if row is not None:
            return row[0]

        self.close_db_connection()

    # end of method

    def open_db_connection(self):
        hostname, username, password, database = self.hostname, self.username, self.password, self.database
        # self.conn_obj = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database, port=3306, use_unicode=True, charset="utf8")
        self.conn_obj = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database,use_unicode=True, charset="utf8")
        self.cursor_obj = self.conn_obj.cursor()

    # end of method

    def close_db_connection(self):
        self.cursor_obj.close()
        self.conn_obj.close()

    # end of method



# end of class defintion