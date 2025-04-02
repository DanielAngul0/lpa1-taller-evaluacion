from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores
from datetime import date # Importa la clase date del modulo datetime para manejar fechas
import random # Importa el modulo 'random' de python para generar valores aleatorios.
import string # Permite la manipulacion de cadenas de texto, ademas, tambien para acceder a caracteres específicos como letras, dígitos o símbolos sin necesidad de escribirlos manualmente

# Instancia de consola para usar rich
console = Console()

# <--- *** Clase Reserva *** --->

# Creando clase Reserva
class Reserva:
    # Definiendo atributos especificos de la clase
    def __init__(self, 
                fecha_inicio: date, 
                fecha_fin: date, 
                estado: str = "Pendiente", 
                codigo_reserva: str = None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.codigo_reserva = codigo_reserva if codigo_reserva is not None else self.generar_codigo()
        
        
    # <--- *** Metodos de clase 'Reserva' *** ---
    
    def generar_codigo(self) -> str:
        # Genera un codigo de reserva unico compuesto de 8 caracteres y un mensaje de confirmacion
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return codigo

    def confirmar_reserva(self):
        # Confirma la reserva, actualizando su estado a "Confirmada"
        self.estado = "Confirmada"
        console.print(f"[bold green]Reserva {self.codigo_reserva} confirmada.[/bold green]")

    def cancelar_reserva(self):
        # Cancela la reserva, actualizando su estado a "Cancelada".
        self.estado = "Cancelada"
        console.print(f"[bold red]Reserva {self.codigo_reserva} cancelada.[/bold red]")

    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'Reserva' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando Reserva ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Código Reserva", self.codigo_reserva)
        tabla.add_row("Fecha Inicio", str(self.fecha_inicio))
        tabla.add_row("Fecha Fin", str(self.fecha_fin))
        tabla.add_row("Estado", self.estado)
        return tabla