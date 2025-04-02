# <--- *** Importaciones necesarias *** --->

# <--- *** Importando las clases con sus atributos y metodos especificos *** --->
# Importando la clase 'Cliente' 
from agencia_de_viajes.cliente import Cliente
# Importando la clase 'AdministradorSistema'
from agencia_de_viajes.administradorsistema import AdministradorSistema
# Importando la clase 'AdministradorHotel'
from agencia_de_viajes.administradorhotel import AdministradorHotel
# Importando la clase 'Hotel'
from agencia_de_viajes.hotel import Hotel
# Importando la clase 'CalendarioOcupacion'
from agencia_de_viajes.calendarioocupacion import CalendarioOcupacion
# Importando la clase 'Habitacion'
from agencia_de_viajes.habitacion import Habitacion
# Importando la clase 'Calificacion'
from agencia_de_viajes.calificacion import Calificacion
# Importando la clase 'SistemaPago'
from agencia_de_viajes.sistemapago import SistemaPago

# <--- *** Importando herramientas extras *** --->
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido 
from datetime import date # Importa la clase date del modulo datetime para manejar fechas


console = Console() # Crea una instancia de la consola para imprimir con colores, estilos y otros formatos mejorados


# <--- *** Creando objetos de cada clase *** --->

def registrar_usuario(usuario):
    # Registrara a un usuario dependiendo su rol(Cliente, Administrador)
    console.print(usuario)
    usuario.registrarse()
    print("=" * 50)


def crear_hotel(nombre, direccion, telefono, correo, ciudad, estado, fechas_ocupadas):
    # Creara un hotel y le asignara un calendario
    calendario = CalendarioOcupacion("Hotel", fechas_ocupadas)
    hotel = Hotel(nombre, direccion, telefono, correo, ciudad, estado)
    hotel.asignar_calendario(calendario)
    console.print(hotel)
    return hotel, calendario


def registrar_administrador_hotel(nombre, telefono, correo, direccion, hotel):
    # Creara un administrador de hotel y le asignara un hotel
    admin = AdministradorHotel(nombre, telefono, correo, direccion)
    console.print(admin)
    admin.registrarse()
    admin.gestionar_hotel(hotel)
    return admin


# <--- *** Registro de Cliente *** --->
cliente = Cliente("Roberto", "95315225", "roB3rt0@gmail.com", "Calle 2 #58-72")
registrar_usuario(cliente)

# <--- *** Metodos de clase 'Cliente' *** --->

# Simular la búsqueda de habitaciones disponibles
habitaciones = cliente.buscar_habitaciones()
if not habitaciones:
    console.print("[bold yellow]No se encontraron habitaciones disponibles.[/bold yellow]")
    
# Simular la reserva de una habitación (puedes reemplazar "Habitación 101" por una instancia real)
cliente.reservar_habitaciones("Habitación 101")
    
# Simular el proceso de pago
cliente.pagar(120.50)

console.print("=" * 50) # Separador


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
    console.print("=" * 50) # Separador


# <--- *** Metodos de clase 'Hotel' *** --->
    
# Visualiza el calendario asignado al hotel
hotel.mostrar_calendario(2023, 4) # (año, mes)
    
# Llamar al método para gestionar servicios
hotel.gestionar_servicios()
    
# Llamar al método para gestionar ofertas
hotel.gestionar_ofertas()
    
# Cambiar el estado del hotel y mostrar el mensaje
hotel.cambiar_estado("Inactivo")

console.print("=" * 50) # Separador

# Creando una habitacion
habitacion1 = Habitacion(
    tipo="Doble",
    descripcion="Habitación con dos camas individuales y vista al mar.",
    precio=120.50,
    capacidad=2,
    reporte_tipo="Mantenimiento",
    reporte_contenido="Se realizó mantenimiento en el baño.",
    reporte_fecha_generacion=date(2024, 3, 15),
    imagenes=["static/images/hawaii.png"],
    estado="Disponible"
)

# Mostrar la información de la habitacion
console.print(habitacion1)


# <--- *** Metodos de clase 'Habitacion' *** --->

# Metodo: Gestion de precios
console.print("[bold underline]Gestión de Precios:[/bold underline]")
habitacion1.gestionar_precio(150.75)  # Actualiza el precio

# Metodo: Gestion de estado
console.print("[bold underline]Gestión de Estado:[/bold underline]")
habitacion1.gestionar_estado("Ocupada")  # Cambia el estado de la habitación

console.print("=" * 50) # Separador


# <--- *** Metodos de clase 'AdministradorSistema' *** --->

# Metodo: Gestionar usuarios
administrador_sistema.gestionar_usuarios()
    
# Metodo: Supervisar plataforma
administrador_sistema.supervisar_plataforma()
    
# Metodo: Auditar transacciones
administrador_sistema.auditar_transacciones()
    
# Metodo: Generar reportes
administrador_sistema.generar_reportes()

console.print("=" * 50) # Separador


# <--- *** Metodos de clase 'Calificacion' *** --->

# Creando algunas instancias de 'Calificacion'
cal1 = Calificacion(4, "Muy buen servicio", date(2023, 4, 10))
cal2 = Calificacion(5, "Excelente atención", date(2023, 4, 15))
cal3 = Calificacion(3, "Servicio regular", date(2023, 4, 20))
    
# Mostrando cada calificacion usando usando la tabla estetica de Rich
console.print(cal1)
console.print(cal2)
console.print(cal3)
    
# Agrupar las calificaciones en una lista
calificaciones = [cal1, cal2, cal3]
    
# Calcular y mostrar el promedio para el hotel y las habitaciones
promedio_hotel = Calificacion.calcular_promedio_hotel(calificaciones)
promedio_habitacion = Calificacion.calcular_promedio_habitacion(calificaciones)
    
console.print(f"[bold green]Promedio de calificaciones del hotel: {promedio_hotel:.2f}[/bold green]")
console.print(f"[bold green]Promedio de calificaciones de la habitación: {promedio_habitacion:.2f}[/bold green]")

console.print("=" * 50) # Separador


# <--- *** Metodos de clase 'SistemaPago' *** --->

sistema_pago = SistemaPago("PagoExpress", 0.05) # Se analiza el nombre del sistema de pago y el porcentaje de comision
console.print(sistema_pago) # Mostrara una tabla estetica reflejando los atributos y datos de 'SistemaPago'
resultado = sistema_pago.procesar_pago(100.0) # Ejecutara la funcion 'procesar_pago' en el objeto creado para calcular 'monto + (monto * comision)' e imprimirlo en resultado
# Logica en caso de que la transaccion falle o se procese corectamente
if resultado:
    console.print("[bold green]El pago se procesó correctamente.[/bold green]")
else:
    console.print("[bold red]El pago falló.[/bold red]")