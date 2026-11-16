print('hola, este es un ejemplo de bucles en python')
print('vamos a ordenar una lista de números ingresados por el usuario')
print('por favor ingrese los números separados por comas (ejemplo: 5,3,8,1):')
print('después de ingresar los números, los ordenaremos de menor a mayor y los mostraremos en pantalla')
print('¡comencemos!')
llista = []
llista.append(input('ingrese un nombre:'))
llista.append(input('ingrese un nombre:'))
llista.append(input('ingrese un nombre:'))
print('Los nombres ingresados son:', llista)
#bucle en un interval concret 

for i in range(17,101):
    if(i%2==0):
     print(i,end=' ')
print('\n')

#bucle en una lista
compt = 0
for i in llista[0]:
    if i=='a':
        compt= compt+1
print('el primer nombre de la lista es:', llista[0], 'y tiene', compt, 'letras a')
print("")

#bucle de bucle amb elements
notes =[[6,6,7,10,9], [10,7,6,7,7], [5,5,10,7,10]]
print("")
compt = 0
for i in notes:
    for j in i:
        if(j==10):
            compt+=1
    print('hi ha', compt, 'deus (10) a la clase')
    
if(compt > 0):
    print('estan asseguts:')
    for i in range(3):
        for j in range(5):
            if(notes[i][j]==10):
                print('en la fila', i, 'columna', j, 'té un 10')
#Fer un programa que demani endevinar un número del 0 al 10 i no pari fins que el trobi utilitzant les notes de clase
import random
numero_secreto = random.randint(0, 10)
while True:
    intento = int(input("Adivina el número (0-10): "))
    if intento == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    else:
        print("Incorrecto. Inténtalo de nuevo.")