import mysql.connector as mariadb


class DBConnector:

    def __init__(self):
        self.host = 'localhost'
        self.database = 'bitnami_opencart'
        self.port = 3306
        self.user = 'bn_opencart'
        self.password = ''

    def my_connection(self):
        """
        Create connection to DB and return cursor
        :return:
        """
        mariadb_connection = mariadb.connect(
            host=self.host,
            database=self.database,
            port=self.port,
            user=self.user,
            password=self.password
        )
        cursor = mariadb_connection.cursor()
        return cursor, mariadb_connection

    def select_method(self, query) -> list:
        """
        Execute SELECT-query and return result
        :param query: SQL-query
        :return: list
        """
        my_curs, my_con = self.my_connection()
        my_curs.execute(query)
        result = my_curs.fetchall()
        my_curs.close()
        my_con.close()
        return result

    def insert_method(self, *args):
        """
        Execute INSERT-query and return result
        :param args: str: should be SQL-queries
        :return:
        """
        my_curs, my_con = self.my_connection()
        for query in args:
            my_curs.execute(query)
        my_con.commit()
        my_curs.close()
        my_con.close()
