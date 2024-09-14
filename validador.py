import re

def validar_contraseña(contraseña):
    # Verifico longitud mínima
    if len(contraseña) < 8:
        return False
    # Verifico mayúsculas
    if not any(char.isupper() for char in contraseña):
        return False
    # Verifico minúsculas
    if not any(char.islower() for char in contraseña):
        return False
    # Verifico números
    if not any(char.isdigit() for char in contraseña):
        return False
    # Verifico caracteres especiales
    if not any(char in '!@#$%^&*' for char in contraseña):
        return False
    return True

# Solicito contraseña al usuario
contraseña = input("Ingresa una contraseña: ")

# Llamar a la función de validación
if validar_contraseña(contraseña):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")