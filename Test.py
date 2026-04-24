''''Escribe un programa en el lenguaje Python para determinar el tipo de dato que corresponde 
a cada uno de los siguientes valores: 
984 
156.89 
"texto" 
True 
[1, 2, 3, 4, 5] 
(1, 2, 3, 4, 5) 
{'nombre': 'Luis', 'edad': 20, 'ciudad': ‘CDMX'} 
Define las variables para contener lo valores anteriores. 
Genera un código para mostrar un mensaje donde se muestre el tipo de ddato de cada valor. 
A continuación, un ejemplo de salida del programa: '''
import math
def TiposDatos():
    var1 = 984
    var2 = 156.89
    var3 = "texto"
    var4 = True 
    var5 = [1, 2, 3, 4, 5] 
    var6 = (1, 2, 3, 4, 5) 
    var7 = {'nombre': 'Luis', 'edad': 20, 'ciudad': 'CDMX'} 
    print("----Tipos de Datos---") 
    Imprime(var1)  
    Imprime(var2)  
    Imprime(var3)  
    Imprime(var4)  
    Imprime(var5)  
    Imprime(var6)  
    Imprime(var7)  
    

def Imprime(var):
    print("El valor " + str(var) + " es de tipo " + str(type(var)))

TiposDatos()
