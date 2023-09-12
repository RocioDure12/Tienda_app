from base.modelo import ModeloBase
from datetime import date

class Orden_compra(ModeloBase):
    id_item:int=None
    id_cliente:int=None
    id_empleado:int=None
    fecha_compra:date=None
    total:float=None