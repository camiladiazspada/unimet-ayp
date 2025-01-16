number=int(input('Ingrese un numero: '))
div=1
sumatoria=0
perfect=False
while number<=0:
    number=int(input('El numero es invalido, ingrese otro: '))
while div < number:
    if number%div==0:
        sumatoria+=div
        if sumatoria==number:
            perfect=True
            break
    div+=1
if perfect:
    print('El numero es perfecto')
else:
    print('El numero no es perfecto')
    

