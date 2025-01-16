#Te contrataron para realizar un programa donde calcule el premio de un juego.

#Los premios son basados en puntos:

#Puntos Premio

   # 1-50 No hay premio
   # 51-150 Bronze
   # 151-180 Plata
   # 181-200 Oro

#Todos los límites inferior y superior aquí son inclusivos, y 
# los puntos solo pueden tomar valores enteros positivos hasta 200.

#En su declaración if, asigne la variable de resultado a un 
# String que contenga el mensaje apropiado según el valor de los puntos.
puntos=float(input('Ingrese el numero de puntos obtenido: '))

if puntos >= 51 and puntos <=150:
    premio='Bronce'
elif puntos>=151 and puntos<=180:
    premio='Plata'
elif puntos>=181 and puntos <=200:
    premio='Oro'
elif puntos <=50 and puntos>=0:
   premio='No hay premio'
if premio=='No hay premio':
   print(f'No hay premio para {puntos}')
else:
   print(f'Felicitaciones, Ganaste la medalla de {premio} por haber tenido {puntos} pts!')