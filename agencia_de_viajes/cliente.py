# Importando clase abstracta Usuario
from agencia_de_viajes.usuario import Usuario # Obtiene los atributos de la clase abstracta Usuario
# Importando la libreria 'Rich'
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores

# Instancia de consola para usar rich
console = Console()


# <--- *** Clase Cliente *** --->

# Creando clase Cliente
class Cliente(Usuario):
    # Tomando los atributos de la clase abstracta Usuario
    def __init__(self, nombre: str, 
                telefono: str, 
                correo_electronico: str, 
                direccion: str):
        super().__init__(nombre, telefono, correo_electronico, direccion)
        # Añadiendo atributos propios de la clase Cliente
        self.reservas_realizadas = [] # Lista para almacenar reservas realizadas
        self.calificaciones = [] # Lista para almacenar calificaciones
        
    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'Cliente' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando nuevo usuario Cliente ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Nombre", self.nombre)
        tabla.add_row("Teléfono", self.telefono)
        tabla.add_row("Correo electrónico", self.correo_electronico)
        tabla.add_row("Dirección", self.direccion)
        return tabla
    
    # Creara un nuevo cliente
    def registrarse(self):
        # Sera representado por su nombre y un mensaje de confirmacion usando 'rich'
        console.print(f"[bold green]Usuario {self.nombre} registrado exitosamente[/bold green]")