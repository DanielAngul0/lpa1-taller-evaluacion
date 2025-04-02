# Importando clase abstracta Usuario
from agencia_de_viajes.usuario import Usuario # Obtiene los atributos de la clase abstracta Usuario
# Importando la libreria 'Rich'
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores

# Instancia de consola para usar rich
console = Console()


# <--- *** Clase AdministradorSistema *** --->

# Creando clase AdministradorSistema
class AdministradorSistema(Usuario):
    # Tomando los atributos de la clase abstracta Usuario
    def __init__(self, nombre: str, 
                telefono: str, 
                correo_electronico: str, 
                direccion: str):
        super().__init__(nombre, telefono, correo_electronico, direccion)
        # Añadiendo atributos propios de la clase AdministradorSistema
        self.auditorias_realizadas = [] # Lista para almacenar las auditorias realizadas
        self.transacciones_supervisadas = [] # Lista para almacenar las transacciones supervisadas
        
    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'AdministradorSistema' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando nuevo usuario Administrador del Sistema ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Nombre", self.nombre)
        tabla.add_row("Teléfono", self.telefono)
        tabla.add_row("Correo electrónico", self.correo_electronico)
        tabla.add_row("Dirección", self.direccion)
        return tabla
    
    # <--- *** Metodos de clase 'AdministradorSistema' *** --->
    
    # Creara un nuevo administrador del sistema
    def registrarse(self):
        # Sera representado por su nombre y un mensaje de confirmacion usando 'rich'
        console.print(f"[bold green]Usuario {self.nombre} registrado exitosamente[/bold green]")
        
    # Simula la gestión de usuarios en la plataforma
    def gestionar_usuarios(self):
        console.print(f"[bold blue]Gestionando usuarios en la plataforma...[/bold blue]")

    # Simula la supervisión del funcionamiento de la plataforma
    def supervisar_plataforma(self):
        console.print(f"[bold blue]Supervisando la plataforma en tiempo real...[/bold blue]")
    
    # Simula la auditoría de transacciones en el sistema   
    def auditar_transacciones(self):
        console.print(f"[bold blue]Auditando transacciones del sistema...[/bold blue]")

    # Simula la generación de reportes del sistema
    def generar_reportes(self):
        console.print(f"[bold blue]Generando reportes del sistema...[/bold blue]")