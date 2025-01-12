from cmath import sqrt
a=float(input("Ingrese el primer lado del triángulo: "))
b=float(input("Ingrese el segundo lado del triángulo: "))
c=float(input("Ingrese el tercer lado del triángulo: "))
s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("El area del triángulo es: ", area)
