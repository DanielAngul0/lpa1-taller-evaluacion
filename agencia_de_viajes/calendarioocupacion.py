import calendar # Importando modulo 'calendar' para trabajar con calendarios
from datetime import date # Importa la clase date del modulo datetime para manejar fechas
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido 
from rich.text import Text # Encargado de aplicar estilos a fragmentos de texto
from rich.panel import Panel # Encargado de encerrar texto en un recuadro decorativo

# Instancia de consola para usar rich
console = Console()


# <--- *** Clase CalendarioOcupacion *** --->

# Creando clase CalendarioOcupacion
class CalendarioOcupacion:
    # Definiendo atributos especificos de la clase
    def __init__(self, tipo_entidad: str, fechas_ocupadas: list):
        self.tipo_entidad = tipo_entidad # 'Hotel' o 'Habitacion'
        self.fechas_ocupadas = fechas_ocupadas

    def mostrar_calendario(self, year: int, month: int):
        #Muestra en consola un calendario del mes y año indicados, los días ocupados se resaltan en rojo.
        
        # Obtener la estructura del mes (lista de semanas; cada semana es una lista de 7 días)
        cal = calendar.monthcalendar(year, month)

        # Encabezado con el nombre del mes y el año
        header_text = Text()
        header_text.append(f"{calendar.month_name[month]} {year}\n", style="bold underline")
        header_text.append("Mo Tu We Th Fr Sa Su\n", style="bold")

        # Construir el cuerpo del calendario
        body_text = Text()

        for week in cal:
            week_line = ""
            for day in week:
                if day == 0:
                    week_line += "   "  # Día en blanco (no pertenece al mes)
                else:
                    current_date = date(year, month, day)
                    if current_date in self.fechas_ocupadas:
                        # Si la fecha está ocupada, se resalta en rojo usando markup de Rich
                        week_line += f"[red]{day:2d}[/red] "
                    else:
                        week_line += f"{day:2d} "
            # Se convierte la línea con markup a un objeto Text
            body_text += Text.from_markup(week_line.rstrip() + "\n")

        # Combinar encabezado y cuerpo
        calendario_text = header_text + body_text

        # Mostrar todo en un Panel
        panel = Panel(calendario_text, title="Calendario de Ocupación", subtitle=self.tipo_entidad, expand=False)
        console.print(panel)
        
    # <--- *** Metodos de clase 'CalendarioOcupacion' *** --->

    def gestionar_disponibilidad(self, year: int, month: int):
        # Simula la gestión de disponibilidad mostrando el calendario para el mes y año indicados
        console.print("[bold green]Gestionando disponibilidad...[/bold green]")
        self.mostrar_calendario(year, month)

    def actualizar_fechas(self, nuevas_fechas: list):
        # Actualiza las fechas ocupadas y muestra un mensaje de confirmación
        self.fechas_ocupadas = nuevas_fechas
        console.print("[bold green]Fechas actualizadas en el calendario de ocupación[/bold green]")
