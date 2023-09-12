from base.modelo import ModeloBase

class Producto(ModeloBase):
    id_categoria:int=None
    id_proveedor:int=None
    nombre:str=None
    cantidad_stock:int=None
    precio_venta:float=None
    precio_al_costo:float=None