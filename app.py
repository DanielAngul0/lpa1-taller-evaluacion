# <--- *** Importaciones necesarias *** --->

# Importando la clase 'Cliente'
from agencia_de_viajes.cliente import Cliente # Obtiene los atributos 
# Importando la clase 'AdministradorSistema'
from agencia_de_viajes.administradorsistema import AdministradorSistema # Obtiene los atributos 
# Importando la clase 'AdministradorHotel'
from agencia_de_viajes.administradorhotel import AdministradorHotel # Obtiene los atributos 


# ---> Creando objetos de cada clase <---


# <--- *** Registro de cliente *** --->

# Datos representados: Nombre, Numero, Correo electronico y direccion propia de cada cliente
cliente = Cliente("Roberto", "95315225", "roB3rt0@gmail.com", "Calle 2 #58-72")

# ---> Imprime datos de los objetos en cadena de texto <---
print(cliente)

# ---> Mensaje confirmacion del usuario registrado <---
cliente.registrarse()

print("=" * 50) # Separador para consola

# <--- *** Registro para administrador del sistema *** --->

# Datos representados: Nombre, Numero, Correo electronico y direccion propia de cada administradorsistema
administradorsistema = AdministradorSistema("Camilo", "521466214", "c4milo@gmail.com", "carrera 72 #8-15")

# ---> Imprime datos de los objetos en cadena de texto <---
print(administradorsistema)

# ---> Mensaje confirmacion del usuario registrado <---
administradorsistema.registrarse()

print("=" * 50) # Separador para consola

# <--- *** Registro para administrador del hotel *** --->

# Datos representados: Nombre, Numero, Correo electronico y direccion propia de cada administradorhotel
administradorhotel = AdministradorHotel("Javier", "5542153690", "Javi@gmail.com", "carrera 2 #78-56")

# ---> Imprime datos de los objetos en cadena de texto <---
print(administradorhotel)

# ---> Mensaje confirmacion del usuario registrado <---
administradorhotel.registrarse()