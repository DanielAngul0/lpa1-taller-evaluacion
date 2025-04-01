# Importando clase abstracta Usuario
from agencia_de_viajes.usuario import Usuario # Obtiene los atributos de la clase abstracta Usuario

# <--- *** Clase AdministradorSistema *** --->

# Creando clase AdministradorSistema
class AdministradorSistema(Usuario):
    # Tomando los atributos de la clase abstracta Usuario
    def __init__(self, nombre: str, telefono: str, correo_electronico: str, direccion: str):
        super().__init__(nombre, telefono, correo_electronico, direccion)
        # Añadiendo atributos propios de la clase AdministradorSistema
        self.auditorias_realizadas = [] # Lista para almacenar las auditorias realizadas
        self.transacciones_supervisadas = [] # Lista para almacenar las transacciones supervisadas
    
    # Creara un nuevo administrador del sistema, sera representado por su nombre y un mensaje de confirmacion
    def registrarse(self):
        print(f"Usuario {self.nombre} registrado exitosamente")