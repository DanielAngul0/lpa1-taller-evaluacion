# Sistema de Agencia de Viajes

![commits](https://badgen.net/github/commits/UR-CC/lp2-taller1?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/UR-CC/lp2-taller1)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor: DanielAngul0

- [DanielAngul0](hhttps://github.com/DanielAngul0)

---

## Descripción del Proyecto

Este proyecto es una simulación de un sistema de gestión para una agencia de viajes, enfocado en la administración de reservas hoteleras. Se implementa en Python y utiliza la librería Rich para proporcionar una salida en consola visualmente atractiva y estructurada.

---

## Documentación

Revisar la documentación en [`./docs`](./docs)

---

### Requerimientos

# 3. Requerimientos Específicos

## 3.1 Requerimientos Funcionales

- **R1**: El sistema debe permitir el registro de hoteles con nombre, dirección, teléfono, correo electrónico y ubicación geográfica.  
- **R2**: El sistema debe permitir la administración de los servicios que ofrece cada hotel (coworking, gimnasio, restaurante, piscina, etc.).  
- **R3**: El sistema debe permitir la gestión de ofertas especiales por temporada y servicios adicionales como estacionamiento y coworking.  
- **R4**: El sistema debe permitir activar o inactivar hoteles según su disponibilidad (cerrado por reformas, mantenimiento, etc.).  
- **R5**: El sistema debe permitir el registro de habitaciones con su tipo, descripción, precio, capacidad y servicios incluidos.  
- **R6**: El sistema debe permitir la carga de imágenes para cada habitación.  
- **R7**: El sistema debe gestionar el estado de las habitaciones (activas, en mantenimiento, en remodelación, etc.).  
- **R8**: El sistema debe mostrar un calendario de ocupación y disponibilidad para cada habitación.  
- **R9**: El sistema debe permitir la modificación dinámica de los precios de las habitaciones según la temporada y el número de huéspedes.  
- **R10**: El sistema debe permitir a los clientes buscar habitaciones aplicando filtros por fecha, ubicación, calificación y precio.  
- **R11**: El sistema debe permitir a los clientes visualizar los detalles completos de una habitación antes de hacer una reserva.  
- **R12**: El sistema debe permitir a los clientes reservar una habitación y generar un código de confirmación.  
- **R13**: El sistema debe permitir la integración con pasarelas de pago para procesar pagos en línea.  
- **R14**: El sistema debe permitir la opción de pago al llegar en caso de que el hotel lo permita.  
- **R15**: El sistema debe generar una confirmación electrónica de la reserva con los detalles de la estancia.  
- **R16**: El sistema debe permitir la cancelación de reservas según las políticas establecidas por cada hotel.  
- **R17**: El sistema debe gestionar reembolsos y penalizaciones según las condiciones de cancelación.  
- **R18**: El sistema debe permitir el registro de clientes con nombre, teléfono, correo electrónico y dirección.  
- **R19**: El sistema debe permitir que los clientes califiquen su estadía y dejen comentarios sobre la habitación y el hotel.  
- **R20**: El sistema debe calcular una calificación promedio para cada habitación basada en las evaluaciones de los clientes.  
- **R21**: El sistema debe calcular una calificación general para cada hotel basada en las calificaciones de sus habitaciones.  
- **R22**: El sistema debe generar reportes sobre reservas, ocupación y desempeño de cada hotel.  
- **R23**: El sistema debe permitir la creación, edición y eliminación de cuentas de administrador del sistema.  
- **R24**: El sistema debe permitir la auditoría de todas las transacciones realizadas en la plataforma.  
- **R25**: El sistema debe contar con un panel de administración para la supervisión general de la plataforma.  

---

## 3.2 Requerimientos No Funcionales

- **R26**: El sistema debe garantizar la seguridad y confidencialidad de los datos personales de clientes y hoteles.  
- **R27**: El sistema debe ser escalable y capaz de manejar múltiples hoteles y reservas sin afectar el rendimiento.  
- **R28**: El sistema debe estar disponible 24/7 y garantizar tiempos de respuesta óptimos.  
- **R29**: El sistema debe ofrecer una interfaz intuitiva y accesible desde dispositivos móviles y computadoras.  
- **R30**: El sistema debe cumplir con estándares de accesibilidad para usuarios con discapacidades.  
- **R31**: El sistema debe permitir auditoría y trazabilidad de todas las acciones realizadas.


---

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/DanielAngul0/lpa1-taller-evaluacion.git
cd lpa1-taller-evaluacion
```
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
---

## Ejecución

Para ejecutar la aplicación, simplemente ejecuta:

1. Ejecutar el proyecto
```bash
python app.py
```

---

## Pruebas Unitarias

El proyecto incluye pruebas unitarias utilizando pytest. Para ejecutar las pruebas, desde la raíz del proyecto ejecuta:

1. Ejecutar el proyecto
```bash
pytest
```