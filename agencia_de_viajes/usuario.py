# Importando clases abstractas para crear metodos abstractos
from abc import ABC, abstractmethod

# <--- *** Clase Abstracta Usuario (Base) *** --->

# Creando clase abstracta Usuario
class Usuario(ABC):
    # Definiendo los atributos de Usuario y agregantole su respectivo tipo de dato
    def __init__(self, nombre: str, 
                telefono: str, 
                correo_electronico: str, 
                direccion: str):
        self.nombre = nombre
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.direccion = direccion
    
    # Toma los atributos de Usuario y lo convierte en un string legible
    def __str__(self):
        return f"""--- Creando nuevo usuario {self.__class__.__name__} ----
Nombre: {self.nombre}
Telefono: {self.telefono}
Correo electronico: {self.correo_electronico}
Direccion: {self.direccion}"""
    
    # Funcion para registrar Usuario dependiendo su rol (Cliente, Administrador del sistema, Administrador del hotel) 
    @abstractmethod
    # Este metodo abstracto creara usuarios con informacion personal de cada uno
    def registrarse(self):
        pass
