from base.servicios import ServiciosBase
from modulos.base.modelo import ModeloBase

class Item_compra_Servicios(ServiciosBase):
    def __init__(self) -> None:
        super().__init__()
    
    def item_a_fila(self, item: ModeloBase) -> dict:
        return super().item_a_fila(item)
    
    def fila_a_item(self, fila: dict) -> ModeloBase:
        return super().fila_a_item(fila)