from cmath import sqrt


a=float(input('Ingrese un valor de a: '))
b=float(input('Ingrese un valor de b: '))
c=float(input('Ingrese un valor de c: '))
argument= (b**2)-(4*a*c)

x1=(-b+sqrt(argument))/2*a
x2=(-b-sqrt(argument))/2*a
if argument<=0:
    print('No puede ejecutarse, puesto que el argumento de la raiz es negativo')
else:
    print(f'El valor de x1 es {x1}: ')
    print(f'El valor de x2 es {x2}: ')

