from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores
from datetime import date # Importa la clase date del modulo datetime para manejar fechas

# Instancia de consola para usar rich
console = Console()

# <--- *** Clase Calificacion *** --->

# Creando clase Calificacion
class Calificacion:
    # Definiendo atributos especificos de la clase
    def __init__(self, 
                puntaje: int,
                comentarios: str,
                fecha: date):
        self.puntaje = puntaje
        self.comentarios = comentarios
        self.fecha = fecha
        
    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'Calificacion' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando Calificacion ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Puntaje", str(self.puntaje))
        tabla.add_row("Comentarios", self.comentarios)
        tabla.add_row("fecha", str(self.fecha))       
        return tabla
    
    
    # <--- *** Metodos de clase 'Calificacion' *** --->
    
    @staticmethod
    # Calculando calificaciones del hotel
    def calcular_promedio_hotel(calificaciones: list) -> float:
        # Calcula el promedio de puntaje para un hotel a partir de una lista de calificaciones: 'calificaciones (list): Lista de objetos Calificacion' devuelve un float con el promedio de la calificacion y retorna 0 si la lista está vacía
        if not calificaciones:
            console.print("[bold red]No hay calificaciones para calcular el promedio del hotel.[/bold red]")
            return 0.0
        total = sum(c.puntaje for c in calificaciones)
        promedio = total / len(calificaciones)
        return promedio

    @staticmethod
        # Calculando calificaciones de las habitaciones
    def calcular_promedio_habitacion(calificaciones: list) -> float:
        # Calcula el promedio de puntaje para un hotel a partir de una lista de calificaciones: 'calificaciones (list): Lista de objetos Calificacion' devuelve un float con el promedio de la calificacion y retorna 0 si la lista está vacía
        if not calificaciones:
            console.print("[bold red]No hay calificaciones para calcular el promedio de la habitación.[/bold red]")
            return 0.0
        total = sum(c.puntaje for c in calificaciones)
        promedio = total / len(calificaciones)
        return promedio