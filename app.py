# <--- *** Importaciones necesarias *** --->

from agencia_de_viajes.cliente import Cliente
from agencia_de_viajes.administradorsistema import AdministradorSistema
from agencia_de_viajes.administradorhotel import AdministradorHotel
from agencia_de_viajes.hotel import Hotel
from agencia_de_viajes.calendarioocupacion import CalendarioOcupacion
from rich.console import Console
from datetime import date

console = Console()  # Consola para impresión mejorada


# <--- *** Funciones para evitar repetición *** --->

def registrar_usuario(usuario):
    """Registra e imprime los datos de un usuario (Cliente o Administrador)."""
    console.print(usuario)
    usuario.registrarse()
    print("=" * 50)


def crear_hotel(nombre, direccion, telefono, correo, ciudad, estado, fechas_ocupadas):
    """Crea un hotel con su respectivo calendario y lo retorna."""
    calendario = CalendarioOcupacion("Hotel", fechas_ocupadas)
    hotel = Hotel(nombre, direccion, telefono, correo, ciudad, estado)
    hotel.asignar_calendario(calendario)
    console.print(hotel)
    return hotel, calendario


def registrar_administrador_hotel(nombre, telefono, correo, direccion, hotel):
    """Crea un administrador de hotel, lo registra y le asigna un hotel."""
    admin = AdministradorHotel(nombre, telefono, correo, direccion)
    console.print(admin)
    admin.registrarse()
    admin.gestionar_hotel(hotel)
    return admin


# <--- *** Registro de Cliente *** --->
cliente = Cliente("Roberto", "95315225", "roB3rt0@gmail.com", "Calle 2 #58-72")
registrar_usuario(cliente)

# <--- *** Registro del Administrador del Sistema *** --->
administrador_sistema = AdministradorSistema("Camilo", "521466214", "c4milo@gmail.com", "carrera 72 #8-15")
registrar_usuario(administrador_sistema)

# <--- *** Registro de Hoteles y sus Administradores *** --->

# Datos de hoteles y administradores
hoteles_info = [
    {
        "hotel": ("Hotel Paraíso", "Av. Principal 123", "555-1234", "contacto@paraiso.com", "Hawaii", "Activo", 
                [date(2023, 4, 10), date(2023, 4, 15), date(2023, 4, 20)]),
        "admin": ("Javier", "5542153690", "Javi@gmail.com", "carrera 2 #78-56"),
        "mes_visualizar": 4
    },
    {
        "hotel": ("Hotel Estrella", "Calle Luna 456", "555-6789", "info@estrella.com", "Jamaica", "Activo", 
                [date(2023, 5, 5), date(2023, 5, 12), date(2023, 5, 25)]),
        "admin": ("Lucia", "300785412", "lucia_hotel@gmail.com", "Avenida 45 #12-30"),
        "mes_visualizar": 5
    }
]

# Registro de los hoteles y administradores
for info in hoteles_info:
    hotel, calendario = crear_hotel(*info["hotel"])
    registrar_administrador_hotel(*info["admin"], hotel)
    
    console.print(f"[bold underline]Calendario de {info['hotel'][0]}:[/bold underline]")
    calendario.gestionar_disponibilidad(2023, info["mes_visualizar"])
    console.print("=" * 50)
