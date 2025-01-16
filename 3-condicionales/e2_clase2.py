#Una famosa cadena de cines en Venezuela te contrató para hacerles un programa de descuento en 
# las entradas basado en la edad del cliente, para ello tendrás que recibir por teclado la edad y 
# nombre del cliente y verificar los siguientes casos:

   # Si su edad es menor o igual a 4 años el precio de su entrada es gratis.
   # Si su edad es menor o igual a 18 años el precio de su entrada es de $1.50
   # Si su edad es mayor o igual a los 60 años su entrada tendrá un valor de $1
   # La entrada para un adulto promedio es de $2.00

#Deberás imprimir un mensaje dependiendo de la edad del cliente para saber el precio de su entrada.

name=(input('Porfavor ingrese su nombre: '))
age=int(input('Ingrese su edad: '))


if age <= 4 and age > 0:
    price=0
elif age >= 18:
    price=1.50
elif age >=60: 
    price=1
elif age >=27 and age <=60:
    price=2.00
print(f'El cliente de nombre{name} y de edad {age}, el precio de su entrada es de {price}')