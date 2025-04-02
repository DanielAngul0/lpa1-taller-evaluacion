# Importando la clase 'CalendarioOcupacion'
from agencia_de_viajes.calendarioocupacion import CalendarioOcupacion # Importa la clase 'CalendarioOcupacion' y obtiene sus atributos 
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores

# Instancia de consola para usar rich
console = Console()

# <--- *** Clase Hotel *** --->

# Creando clase Hotel
class Hotel:
    # Definiendo atributos especificos de la clase
    def __init__(self, 
                nombre: str, 
                direccion: str, 
                telefono: str, 
                correo_electronico: str, 
                ubicacion: str, 
                estado: str, 
                calendario: CalendarioOcupacion = None):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.ubicacion = ubicacion
        self.estado = estado
        self.calendario = calendario

    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'Hotel' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando Hotel ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Nombre", self.nombre)
        tabla.add_row("Direccion", self.direccion)
        tabla.add_row("Teléfono", self.telefono)
        tabla.add_row("Correo electrónico", self.correo_electronico)
        tabla.add_row("Ubicacion", self.ubicacion)
        tabla.add_row("Estado", self.estado)
        return tabla

    def asignar_calendario(self, calendario: CalendarioOcupacion):
        # Asigna el calendario de ocupación para el hotel
        if not isinstance(calendario, CalendarioOcupacion):
            console.print("[bold red]Error:[/bold red] El objeto asignado no es un CalendarioOcupacion.")
            return
        self.calendario = calendario
        console.print(f"[bold green]Calendario asignado al hotel {self.nombre}.[/bold green]")
        
    # Simula la gestión de los servicios del hotel
    def gestionar_servicios(self):
        console.print(f"[bold blue]Gestionando servicios para el hotel {self.nombre}.[/bold blue]")
    
    # Simula la gestión de ofertas para el hotel
    def gestionar_ofertas(self):
        console.print(f"[bold blue]Gestionando ofertas para el hotel {self.nombre}.[/bold blue]")

    # Cambia el estado actual de un hotel y se asegura que sea un estado valido 
    def cambiar_estado(self, nuevo_estado: str):
        estados_validos = ["Activo", "Inactivo", "Mantenimiento", "Cerrado"]
        if nuevo_estado not in estados_validos:
            console.print(f"[bold red]Error:[/bold red] Estado '{nuevo_estado}' no es válido.")
            return
        
        estado_anterior = self.estado
        self.estado = nuevo_estado
        # Mostrara un mensaje confirmando el cambio
        console.print(f"[bold yellow]El estado del hotel {self.nombre} ha cambiado de {estado_anterior} a {nuevo_estado}.[/bold yellow]")

    # Muestra el calendario si este ya tiene una asignado
    def mostrar_calendario(self, year: int, month: int):
        """Muestra el calendario del hotel si tiene uno asignado."""
        if self.calendario:
            self.calendario.mostrar_calendario(year, month)
        else:
            console.print(f"[bold red]Error:[/bold red] El hotel {self.nombre} no tiene un calendario asignado.")