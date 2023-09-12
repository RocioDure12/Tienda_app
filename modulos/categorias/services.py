from base.servicios import ServiciosBase
from ..categorias.modelo import Categoria

class CategoriaServicios(ServiciosBase):
    def __init__(self):
        pass
    
    def item_a_fila(self, item: Categoria) -> dict:
        data=ServiciosBase.item_a_fila(self,item)
        data['nombre']=f"'{item.nombre}'"
        return data
    
    
    def fila_a_item(self, fila: dict) -> Categoria:
        item:Categoria=ServiciosBase.fila_a_item(self, fila)
        item.nombre=fila['name']
        return item
       