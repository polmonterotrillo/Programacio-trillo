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
    if(i=='a'):
        compt+=1
print('el primer nombre de la lista es:', llista[0], 'y tiene', compt, 'letras a')
print("")

#bucle de bucle amb elements



