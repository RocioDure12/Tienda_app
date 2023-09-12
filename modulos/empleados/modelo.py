from base.modelo import ModeloBase

class Empleado(ModeloBase):
    nombre:str=None
    apellido:str=None
    cargo:str=None
    id_supervisor:int=None