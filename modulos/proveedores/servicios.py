from ..base.servicios import ServiciosBase
from .modelo import Proveedor

class ServiciosProveedores(ServiciosBase):

    def item_a_fila(self, item:Proveedor)->dict:
        data={}
        return data
    

    def fila_a_item(self, fila:dict)->Proveedor:
         item=Proveedor()
         item.id=fila['id']
         return item
         
   
    def fila_a_sql(self,fila:dict):
         sql=''
         for key in fila:
             sql+=f"{key}={fila[key]},"
         return sql.rstrip(",")
