'''
var = 1
var2 = 2.5
var3 = "Hola grupo"

print("La variable 1 es tipo: " + str(type(var)) + " La variable 2 es tipo: " + str(type(var2)))

arreglo = [1,4,3,5]


dicc = {'A': 10, 'B': 15, 'C': 10}

tup = (1,2,3)


if var > 1:
    print("El valor es mayor que uno")
else:
    print("El valor es menor que uno")

print("valores del arreglo")

for i in arreglo:
    print(i)
    

for i_key in dicc:
    print(i_key, dicc[i_key])

while var != 1:
    print("El valor es diferente que uno")
'''

nombre = input("Cual es tu nombre?")

print("Te llamas: " + nombre)





