num=int(input('Ingrese un numero '))
is_prime=True
div=2
while div<num:
    if num%div==0:
        is_prime=False
        break
    div+=1
if is_prime:
    print(f'El numero {num} es primo')
else:
    print(f'El numero {num} NO es primo')
