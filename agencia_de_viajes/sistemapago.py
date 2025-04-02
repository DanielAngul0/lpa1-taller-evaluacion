from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores

# Instancia de consola para usar rich
console = Console()

# <--- *** Clase SistemaPago *** --->

# Creando clase SistemaPago
class SistemaPago:
    # Definiendo atributos especificos de la clase
    def __init__(self, 
                nombre: str, 
                comision: float):
        self.nombre = nombre
        self.comision = comision
        
    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def __rich__(self):
        # Creando titulo para la clase 'SistemaPago' y columnas de la tabla con estetica
        tabla = Table(title="--- Creando SistemaPago ---", style="bold cyan")
        tabla.add_column("Atributo", style="bold yellow", no_wrap=True)
        tabla.add_column("Valor", style="#005DF4")
        
        # Creando filas de la tabla y añadiendo atributos especificos en formato string
        tabla.add_row("Nombre", self.nombre)
        tabla.add_row("Comisión", f"{self.comision*100:.1f}%")
        return tabla
    
    # <--- *** Metodos de clase 'SistemaPago' *** ---
    
    def procesar_pago(self, monto: float) -> bool:
        # Simula el procesamiento de un pago, aplicando la comision y calculando el total a pagar
        total = monto + (monto * self.comision)
        # Mostrara el monto original, comision aplicada y el total a pagar
        console.print(f"[bold green]Procesando pago con {self.nombre}:[/bold green]")
        console.print(f"[bold blue]Monto original:[/bold blue] {monto:.2f}")
        console.print(f"[bold blue]Comisión aplicada:[/bold blue] {self.comision*100:.1f}%")
        console.print(f"[bold blue]Total a pagar:[/bold blue] {total:.2f}")
        return True