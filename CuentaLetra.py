'''Hacer un programa en el que se pregunte al usuario por una frase
y una letra, y muestre por pantalla el número de veces que aparece 
la letra en la frase.'''

Frase = input("Ingresa una frase: ")
Letra = input("Ingresa una letra: ")

cont = 0

for i in Frase:
    if i == Letra:
        cont += 1

#print("La frase '" + Frase + "' tiene la letra '" + Letra + "' " + str(cont) + " veces.")
print(f"En el texto '{Frase}', la letra '{Letra}' aparece {cont} veces.")
