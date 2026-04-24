TornilloAcero = [7,3,5,65]
TornilloHormigon = [6,4,4,85]
ClavoGalvanizado =[4,57]

def Menu():
    print("Bienvenido a tu validador de materiales")
    opcion = int(input("Ingresa la opción deseada:\n 1.-Validar Tornillo de Acero Inoxidable \n 2.-Validar Tornillo de Hormigon \n 3.-Validar Clavo Hormigon \n "))
    if opcion == 1:
        medidas = SolicitarDatos(opcion)
        if not MedidasTornillo(medidas, TornilloAcero):
            print("El tornillo no tiene las medidas correctas")
        else:
            print("El tornillo tiene las medidas correctas, continue con la siguiente etapa.")

def MedidasTornillo(Medidas, TornilloValidar):
    resultado = True
    tornillo = TornilloValidar 
    for i in tornillo:          
        if Medidas[tornillo.index(i)] != i:         
            Resultado = False           
            break
    return Resultado         

def MedidasClavo(Medidas):
    Resultado = True    
    for i in ClavoGalvanizado:        
        if Medidas[ClavoGalvanizado.index(i)] != i:         
            Resultado = False           
            break
    return Resultado       


def SolicitarDatos(opcion):
    medidas = []
    if opcion == 1 or opcion == 2:
        medidas.append(int(input("Ingresa la medida del diametro: ")))
        medidas.append(int(input("Ingresa la medida de la altura: ")))
        medidas.append(int(input("Ingresa la medida del cuello: ")))
        medidas.append(int(input("Ingresa la medida de la rosca: ")))
    else:
        medidas.append(int(input("Ingresa la medida de la cabeza: ")))
        medidas.append(int(input("Ingresa la medida de la caña: ")))
    return medidas

Menu()