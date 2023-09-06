from abc import abstractmethod
from abc import ABC
from ..base.modelo import ModeloBase
from typing import List

class ServiciosBase(ABC):
    def item_a_fila(self, item:ModeloBase)->dict:
        data=item.__dict__
        return data
    
    def fila_a_item(self, fila:dict)->ModeloBase:
        #recibe un dict y lo transforma en una instancia de la clase ModeloBase 
         item=ModeloBase()
         item.id=fila['id']
         return item
         
    
    def fila_a_sql(self,fila:dict):
        #recibe un dict () y lo transforma en una cadena sql (str)
         print("p")
         sql=str(fila)
         return sql
         
         