#Realice un algoritmo que dado un número, tiene que imprimir:

#En el caso de que el número sea divisible por 3 fizz.

#En el caso de que el número sea divisible por 5 buzz.

#En el caso de que sea divisible por 3 y por 5 fizzbuzz.

#En caso contrario imprima el número

number=int(input('Ingrese un numero: '))

while number%3==0 and number%5==0:
    break
print(number)
if number%3==0 and not number%5==0:
    print(f'El {number} es divisible entre 3')
elif number%5==0 and not number%3==0:
    print(f'El {number} es divisible entre 3 y 5 ')
else:
    print(number)


