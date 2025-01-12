#Escribe un programa en donde pidas por teclado el nombre y el año de nacimiento de la persona y 
# muestre como resultado el siguiente mensaje:
name=str(input("Ingrese su nombre"))
birth_year=int(input("Ingrese su año de nacimiento"))
age= 2025-birth_year
print(name,"cumplió o cumplirará",age,"años este año")