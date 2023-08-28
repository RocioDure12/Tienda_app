import pymysql
from typing import List

class BDServices:
    def conexion_bd(self) -> pymysql.Connection:
        return pymsql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='tienda',
            cursorclass=pymysql.cursors.DictCursor
            
            
        )
        
    def execute_db(self, sql:str) -> int:
            connection = self.connect_db()
            with connection.cursor() as cursor:
                cursor.execute(sql)
            connection.commit()
            return connection.affected_rows()


    def query_db(self, sql:str) -> List[dict]:
        connection = self.connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()