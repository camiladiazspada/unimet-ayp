#Realizar un programa donde se reciba un número flotante por teclado e imprima un mensaje diciendo si el número es 
#par o impar y evaluar si es positivo/negativo.
number=float(input('Ingrese un número: '))

es_par: bool=True
if number % 2== 0 :
    es_par=True
else:
    es_par=False


es_positivo: bool=True
if number >=0:
    es_positivo=True
else:
    es_positivo=False

print(f'El numero {number} es {es_par} y {es_positivo}.')
