import pymysql
from typing import List


class Servicios_BD:
    
    def conexion_bd(self) -> pymysql.Connection:
        return pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='tienda',
            cursorclass=pymysql.cursors.DictCursor

        )
        
    #funcion que ejecuta operacion de escritura en bd
    def operacion_escritura(self, sql:str)->int:
            connection = self.conexion_bd()
            with connection.cursor() as cursor:
                cursor.execute(sql)
            connection.commit()
            return connection.affected_rows()
        
    #Ejecuta una operación de lectura en db
    def operacion_lectura(self,sql:str) -> List[dict]:
            connection = self.conexion_bd()
            with connection.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        
    