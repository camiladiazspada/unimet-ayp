q1=float(input("Ingrese la carga de la particula 1: "))
q2=float(input("Ingrese la carga de la particula 2: "))
r=float(input("Ingrese la distancia existente: "))
k=8.85e-12
fuerza_electrica= k*((q1*q2)/r**2)
print( "La magnitud de la fuerza: ", fuerza_electrica)
