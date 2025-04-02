from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores
from datetime import date # Importa la clase date del modulo datetime para manejar fechas

# Instancia de consola para usar rich
console = Console()

# <--- *** Clase Pago *** --->

# Creando clase Pago
class Pago:
    # Definiendo atributos especificos de la clase
    def __init__(self, 
                monto: float, 
                metodo_pago: str,
                fecha_pago: date,
                opcion_pago_al_llegar: bool,
                estado: str):
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.fecha_pago = fecha_pago
        self.opcion_pago_al_llegar = opcion_pago_al_llegar
        self.estado = estado
        
        # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'Pago' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando Pago ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Monto", f"${self.monto:.2f}")
        tabla.add_row("Método de Pago", self.metodo_pago)
        tabla.add_row("Fecha de Pago", str(self.fecha_pago))
        tabla.add_row("Pago al Llegar", "Sí" if self.opcion_pago_al_llegar else "No")
        tabla.add_row("Estado", self.estado)
        return tabla
    
    # <--- *** Metodos de clase 'Pago' *** ---
    
    def procesar_pago(self):
        # Simula el procesamiento del pago
        console.print(f"[bold green]Procesando pago de ${self.monto:.2f} usando {self.metodo_pago}...[/bold green]")
        self.estado = "Procesado"
        console.print(f"[bold blue]Estado del pago: {self.estado}[/bold blue]")
        return True

    def gestionar_reembolso(self):
        # Simula la gestión de un reembolso.
        console.print(f"[bold yellow]Iniciando proceso de reembolso para un pago de ${self.monto:.2f}...[/bold yellow]")
        # Se cambia el estado a 'Reembolsado'
        self.estado = "Reembolsado"
        console.print(f"[bold blue]Estado del pago: {self.estado}[/bold blue]")
    