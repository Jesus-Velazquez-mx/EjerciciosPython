var9 = 9
print(type(var9))
print("EL valor " + str(var9) + " es de tipo " + str(type(var9)))
lista = [1,2,3,4]
for i in lista:
    print(i)

print(lista)

dicc = {'A':5, 'B':10, 'C':15}

for d_key in dicc:
    print(d_key, dicc[d_key])

print(dicc)

a = 8 
if a < 10:
    print("a es menor a 10")
else:
    print("a no es menor a 10")

nombre = input("Ingresa tu nombre:")
print("Te llamas: " + nombre) 

print("Los valores " + str(lista) + " son de tipo "+ str(type(lista)))
print("Los valores " + str(dicc) + " son de tipo "+ str(type(dicc)))