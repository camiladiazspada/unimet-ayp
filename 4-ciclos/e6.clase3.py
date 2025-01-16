#Dado un número entero de n cifras realice un algoritmo capaz de voltear las cifras (e.g. 132 -> 231)
number=int(input('Ingrese un numero: '))
resultado=0

while number>0:
    #extraigo el ultimo digito en este paso
    digito=number%10
    #Se lo agrego a lo que me invertira para "desplazar" los dígitos existentes a la izquierda.
    resultado=resultado*10+digito
    #Eliminamos el ultimo digito del numero original con una division exacta
    number//=10
if number < 0:
        resultado = -resultado

print(resultado)