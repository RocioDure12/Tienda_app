from abc import abstractmethod
from abc import ABC
from ..base.modelo import ModeloBase
from typing import List

class ServiciosBase(ABC):
    def item_a_fila(self):
        #objeto (tipo modelo base a fila )
        print("p")
    
    
    def fila_a_item(self):
        #
         print("p")
    
    def fila_a_sql(self):
        #
         print("p")