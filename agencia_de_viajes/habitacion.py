from datetime import date # Importa la clase date del modulo datetime para manejar fechas
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores

# Instancia de consola para usar rich
console = Console()

# <--- *** Clase Habitacion *** --->

# Creando clase Habitacion
class Habitacion:
    # Definiendo atributos especificos de la clase
    def __init__(self, 
                tipo: str,
                descripcion: str,
                precio: float,
                capacidad: int,
                reporte_tipo: str = "",
                reporte_contenido: str = "",
                reporte_fecha_generacion: date = None,
                imagenes: list = None,
                estado: str = "Disponible"):
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio = precio
        self.capacidad = capacidad
        self.reporte_tipo = reporte_tipo
        self.reporte_contenido = reporte_contenido
        self.reporte_fecha_generacion = reporte_fecha_generacion
        self.imagenes = imagenes if imagenes is not None else []
        self.estado = estado
        
    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'Habitacion' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando Habitacion ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Tipo", self.tipo)
        tabla.add_row("Descripción", self.descripcion)
        tabla.add_row("Precio", f"${self.precio:.2f}")
        tabla.add_row("Capacidad", str(self.capacidad))
        tabla.add_row("Reporte Tipo", self.reporte_tipo if self.reporte_tipo else "N/A")
        tabla.add_row("Reporte Contenido", self.reporte_contenido if self.reporte_contenido else "N/A")
        tabla.add_row("Fecha Reporte", str(self.reporte_fecha_generacion) if self.reporte_fecha_generacion else "N/A")
        tabla.add_row("Imagenes", ", ".join(self.imagenes) if self.imagenes else "No hay imagen")
        tabla.add_row("Estado", self.estado)
        return tabla
    
    
    # <--- *** Metodos de clase 'Habitacion' *** --->
    
    def gestionar_precio(self, nuevo_precio: float):
        #Actualiza el precio de la habitación y muestra un mensaje de confirmación
        precio_anterior = self.precio
        self.precio = nuevo_precio
        console.print(f"[bold green]Precio de la habitación actualizado de ${precio_anterior:.2f} a ${nuevo_precio:.2f}.[/bold green]")

    def gestionar_estado(self, nuevo_estado: str):
        #Cambia el estado de la habitación
        estado_anterior = self.estado
        self.estado = nuevo_estado
        # Muestra un mensaje confirmando
        console.print(f"[bold yellow]Estado de la habitación cambiado de '{estado_anterior}' a '{nuevo_estado}'.[/bold yellow]")