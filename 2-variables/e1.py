# Se le ha dado un conjunto de variables para que le realice modificaciones.
# 1. Disminuir la variable de lluvia en un 10% para tener en cuenta el agua de lluvia que circula libremente 
#    sobre la superficie de un terreno.
# 2. Agregue la variable de lluvia a la variable volumen_reservorio.
# 3. Aumentar volumen_reservorio en un 5% para tener en cuenta las aguas pluviales que fluyen en el embalse en los días posteriores a la tormenta.
# 4. Disminuir volumen_reservorio en un 2% para tener en cuenta la evaporación.
# 5. Resta 2.5e5 metros cúbicos de volumen_reservorio para tener en cuenta el agua que se canaliza a regiones áridas.
# 6. Imprime el nuevo valor de la variable volumen_reservorio.

volumen_reservorio: float = 4.445e8
lluvia: float = 5e6

print("VOLUMEN RESERVORIO ORIGINAL = ", volumen_reservorio,)

# 10% del Volumen reservatorio
lluvia -= lluvia * 0.1
print("VOLUMEN RESERVORIO DISMINUIDO EN 10% = ", volumen_reservorio)
#Agregar lluvia a volumen
volumen_reservorio+=lluvia
print("VOLUMEN RESERVORIO + LLUVIA =", volumen_reservorio)
#Aumentar 5%
volumen_reservorio+= volumen_reservorio*0.05
print("VOLUMEN RESERVORIO AUMENTADO EN 5% ", volumen_reservorio)
#Disminuir 2%
volumen_reservorio-= volumen_reservorio*0.02
print("VOLUMEN RESERVORIO DISMINUIDO EN 2%", volumen_reservorio)
#Restar los metros cubicos
volumen_reservorio-=2.5e5
print("Nuevo valor de volumen reservorio ",volumen_reservorio)
