# <--- *** Importaciones necesarias *** --->

# Importando framework de testeo
import pytest
# Importando la clase 'Hotel'
from agencia_de_viajes.hotel import Hotel
# Importando la clase 'Reserva'
from agencia_de_viajes.reserva import Reserva
# Importando la clase 'Pago'
from agencia_de_viajes.pago import Pago
# Importando la clase 'SistemaPago'
from agencia_de_viajes.sistemapago import SistemaPago
# Importando la clase 'Calificacion'
from agencia_de_viajes.calificacion import Calificacion
# Importa la clase date del modulo datetime para manejar fechas
from datetime import date 


# --- Prueba 1: Crear de un Hotel ---
def test_creacion_hotel():
    hotel = Hotel("Hotel Central", "Calle 123", "123456789", "contacto@hotel.com", "Ciudad", "Disponible")
    assert hotel.nombre == "Hotel Central"
    assert hotel.estado == "Disponible"

# --- Prueba 2: Crear de una Reserva ---
def test_creacion_reserva():
    # Se crea una reserva con fechas de inicio y fin, estado "Pendiente" por defecto y código autogenerado
    reserva = Reserva(date(2025, 5, 20), date(2025, 5, 25))
    assert reserva.estado == "Pendiente"
    # Se espera que el codigo generado tendra 8 caracteres
    assert isinstance(reserva.codigo_reserva, str)
    assert len(reserva.codigo_reserva) == 8

# --- Prueba 3: Pago procesado exitosamente ---
def test_pago_procesado():
    # Se crea un pago con estado "Pendiente" y se procesa
    pago = Pago(500.0, "Tarjeta de Crédito", date.today(), False, "Pendiente")
    resultado = pago.procesar_pago()
    assert resultado is True
    assert pago.estado == "Procesado"

# --- Prueba 4: Gestion de reembolso ---
def test_pago_reembolso():
    pago = Pago(500.0, "Tarjeta de Crédito", date.today(), False, "Pendiente")
    pago.procesar_pago()  # Procesa el pago y lo marca como 'Procesado'
    pago.gestionar_reembolso()
    assert pago.estado == "Reembolsado"

# --- Prueba 5: Calculando el promedio de calificaciones para un hotel ---
def test_promedio_calificaciones_hotel():
    calificaciones = [
        Calificacion(5, "Excelente servicio", date(2025, 1, 1)),
        Calificacion(3, "Regular", date(2025, 2, 1)),
        Calificacion(4, "Bueno", date(2025, 3, 1))
    ]
    promedio = Calificacion.calcular_promedio_hotel(calificaciones)
    # El promedio esperado es (5 + 3 + 4) / 3 = 4.0
    assert abs(promedio - 4.0) < 0.01

# --- Prueba 6: Calculando el promedio de calificaciones para una habitacion ---
def test_promedio_calificaciones_habitacion():
    calificaciones = [
        Calificacion(2, "Malo", date(2025, 1, 1)),
        Calificacion(3, "Regular", date(2025, 2, 1)),
        Calificacion(5, "Excelente", date(2025, 3, 1))
    ]
    promedio = Calificacion.calcular_promedio_habitacion(calificaciones)
    # El promedio esperado es (2 + 3 + 5) / 3 ≈ 3.33
    assert abs(promedio - 3.33) < 0.01