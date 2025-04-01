# Importando clase abstracta Usuario
from agencia_de_viajes.usuario import Usuario # Obtiene los atributos de la clase abstracta Usuario

# <--- *** Clase AdministradorHoltel *** --->

# Creando clase AdministradorHoltel
class AdministradorHotel(Usuario):
    # Tomando los atributos de la clase abstracta Usuario
    def __init__(self, nombre: str, telefono: str, correo_electronico: str, direccion: str):
        super().__init__(nombre, telefono, correo_electronico, direccion)
        # Añadiendo atributos propios de la clase AdministradorHotel
        self.hoteles_gestionados = []
        self.politicas_cancelaciones = []
        
    # Creara un nuevo administrador de hotel, sera representado por su nombre y un mensaje de confirmacion
    def registrarse(self):
        print(f"Usuario {self.nombre} registrado exitosamente")