# Importando clase abstracta Usuario
from agencia_de_viajes.usuario import Usuario # Obtiene los atributos de la clase abstracta Usuario
# Importando la clase 'AdministradorHotel'
from agencia_de_viajes.hotel import Hotel # Obtiene los atributos
# from agencia_de_viajes.hotel import Hotel Obtiene los atributos
# Importando la libreria 'Rich'
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores

# Instancia de consola para usar rich
console = Console()

# <--- *** Clase AdministradorHotel *** --->

# Creando clase AdministradorHotel
class AdministradorHotel(Usuario):
    # Tomando los atributos de la clase abstracta Usuario
    def __init__(self, 
                nombre: str, 
                telefono: str, 
                correo_electronico: str, 
                direccion: str):
        super().__init__(nombre, telefono, correo_electronico, direccion)
        # Añadiendo atributos propios de la clase AdministradorHotel
        self.hoteles_gestionados = [] # Lista para almacenar los hoteles gestionados
        self.politicas_cancelaciones = [] # Diccionario para almacenar las políticas de cancelación
        
    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'AdministradorHotel' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando nuevo usuario Administrador de Hotel ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Nombre", self.nombre)
        tabla.add_row("Teléfono", self.telefono)
        tabla.add_row("Correo electrónico", self.correo_electronico)
        tabla.add_row("Dirección", self.direccion)
        return tabla
        
    # Creara un nuevo administrador de hotel
    def registrarse(self):
        # Sera representado por su nombre y un mensaje de confirmacion usando 'rich'
        console.print(f"[bold green]Usuario {self.nombre} registrado exitosamente[/bold green]")
    
    # Asignara los administradores existentes a un hotel en especifico    
    def gestionar_hotel(self, hotel: Hotel):
        # Agrega el hotel a la lista de 'hoteles_gestionados'
        self.hoteles_gestionados.append(hotel)
        # Generara un mensaje confirmando la asignacion del 'Administrador de hotel' hacia un 'Hotel' en especifico
        console.print(f"[bold green]El Administrador [cyan]{self.nombre}[/cyan] ahora gestiona el hotel:[/bold green] [cyan]{hotel.nombre}[/cyan]")
    
    # Define el precio que recibira el hotel    
    def definir_precios(self, hotel: Hotel, precio_nuevo):
        # Generara un mensaje confirmando el cambio de precio del hotel
        console.print(f"[bold yellow]El Administrador [cyan]{self.nombre}[/cyan] ha cambiado el precio del hotel {hotel.nombre} a:[/bold yellow] [bold red]{precio_nuevo}[/bold red]")
    
    # Simula la administración de reservas para todos los hoteles gestionados    
    def administrar_reservas(self):
        console.print(f"[bold magenta]El Administrador [cyan]{self.nombre}[/cyan] está administrando las reservas de los hoteles gestionados.[/bold magenta]")