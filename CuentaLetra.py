'''Hacer un programa en el que se pregunte al usuario por una frase
y una letra, y muestre por pantalla el número de veces que aparece 
la letra en la frase.'''

Frase = input("Ingresa una frase: ")
Letra = input("Ingresa una letra: ")

def CuentaFrase(Frase, Letra):
    cont = 0
    for i in Frase:
        if i == Letra:
            cont += 1
    return cont

Contador = CuentaFrase(Frase, Letra)
print("La frase '" + Frase + "' tiene la letra '" + Letra + "' " + str(Contador) + " veces.")