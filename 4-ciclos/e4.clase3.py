#Realiza un algoritmo que reciba y sume números enteros positivos, 
#hasta que reciba un número negativo, ahí pare e imprima el total sumado

number=int(input('Ingrese un numero '))
sumatoria=0

while sumatoria>=0 :
    number+=sumatoria
    sumatoria=int(input('Ingrese otro numero: '))
    if  sumatoria==float or sumatoria<=0:
        break
print(number)
    



