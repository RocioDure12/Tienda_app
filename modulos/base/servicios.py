from abc import abstractmethod
from abc import ABC
from ..base.modelo import ModeloBase
from typing import List

class ServiciosBase(ABC):
    @abstractmethod
    def fila_a_sql(self, item:dict):
        sql=""
        for key in item:
            sql+=f"{key}={item[key]},"
        return sql.rstrip(",")

    @abstractmethod
    def item_a_fila(self, item:ModeloBase)->dict:
        data={}
        return data
    
    def fila_a_item(self, fila:dict)->ModeloBase:
        item=ModeloBase()
        item.id=fila['id']
        return item
        