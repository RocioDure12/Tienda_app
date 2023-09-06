from modulos.bd.servicios import Servicios_BD
from modulos.base.modelo import ModeloBase
from modulos.base.servicios import ServiciosBase

#cli_services=CLIservices()
#cliente_n1=cli_services.prompt_cliente()  
base_datos=Servicios_BD()
conexion=base_datos.conexion_bd()
Servicios_Base=ServiciosBase()


"""
-tenemos objeto ModeloBase que es un object 
-Para por ejemplo guardar eso en la base de datos 
"""

#cliente=ModeloBase('Richard','Coleman','rickycole@gmail.com','3434568689')
#Esto no funciona porque las clases abstractas no se instancian directamente


class Cliente(ModeloBase):
    nombre:str=None
    apellido:str=None
    email:str=None
    telefono:str=None

class CLIservices:
    def prompt_cliente(self)->Cliente:
        cliente=Cliente()
        cliente.nombre=input('nombre: ')
        cliente.apellido=input('apellido: ')
        cliente.email=input('email: ')
        cliente.telefono=input('telefono: ')
        return cliente


#nuevo_proveedor="INSERT INTO proveedores(nombre,email,telefono) VALUES ('RocioSRL','iguana@gmail.com','4356978')"
#nuevo=base_datos.operacion_escritura(nuevo_proveedor)
consulta='select * from proveedores'
results=base_datos.operacion_lectura(consulta)
print(results)#Lista de diccionarios

#item to row objeto a fila (registro)
#row to sql fila a string sql
#row to item fila a objeto 

#TypeError: Can't instantiate abstract class ServiciosBase with abstract methods fila_a_item, fila_a_sql, item_a_fila
class ejemplo(ModeloBase):
    nombre:str=None
    apellido:str=None

instancia=ejemplo()
instancia.nombre="Lore"
instancia.apellido="Ope"

objeto_1=Servicios_Base.item_a_fila(instancia)