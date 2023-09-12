from ..base.modelo import ModeloBase

class Item(ModeloBase):
    id_producto:int=None
    id_proveedor:int=None
    id_orden_compra:int=None
    cantidad:int=None
    precio_unitario:float=None

