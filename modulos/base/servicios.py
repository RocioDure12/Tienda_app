from abc import abstractmethod
from abc import ABC
from ..base.modelo import ModeloBase


class ServiciosBase(ABC):
    @abstractmethod
    def item_a_fila(self, item:ModeloBase)->dict:
        data=item.__dict__
        return data
    
    @abstractmethod
    def fila_a_item(self, fila:dict)->ModeloBase:
        #recibe un dict y lo transforma en una instancia de la clase ModeloBase 
         item=ModeloBase()
         item.id=fila['id']
         return item
         
    @abstractmethod
    def fila_a_sql(self,fila:dict):
        #recibe un dict () y lo transforma en una cadena sql (str)
         sql=''
         for key in fila:
             sql+=f"{key}={fila[key]},"
         return sql.rstrip(",")
         
         

