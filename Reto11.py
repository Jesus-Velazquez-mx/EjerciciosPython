rentaTotal = 0
seguroMenor = 0
licencia = ""
edad = 0
diasRenta = 0
modelo = ""

def IngresaInformacion():
    print("Bienvenido a tu cotizador de renta de autos")
    licencia = input("Ingresa el identificador de tu licencia: ")
    edad = int(input("Ingresa tu edad: "))
    diasRenta = int(input("Cuántos días deseas rentar el automovil: "))
    if diasRenta < 3:
        respuesta = input("El número de días de renta es mínimo 3, desea continuar con la cotización (S/N)?: ")
        if respuesta == "S":
            diasRenta = int(input("Ingrese de nuevo los días a rentar el automovil: "))
    modelo = input("Ingresa el modelo(Año) del vehiculo que desea rentar: ")
    GeneraCotizacion(licencia,edad,diasRenta,modelo)          

def imprimirCotizacion(licencia,edad,rentaTotal,seguroMenor = 0):
    print("Estimado cliente con número de licencia: " + licencia)
    if edad >= 15 and edad <= 18:
        print("Cliente tipo: menor de edad (Autorización tutor/aval)")
        print("Subtotal: $" + str(rentaTotal))
        print("Seguro menor edad: $" + str(seguroMenor))
        print("Total a pagar: $" + str(rentaTotal + seguroMenor))
        print("** Una vez entregada la unidad se reembolsa el seguro menor edad.")
    else:
        print("Subtotal: $" + str(rentaTotal))
        print("Total a pagar: $" + str(rentaTotal))

def GeneraCotizacion(licencia, edad, diasRenta, modelo):
    match(modelo):
        case "2017":
            rentaTotal = 550 * diasRenta 
        case "2018":
            rentaTotal = 590 * diasRenta 
        case "2019":
            rentaTotal = 650 * diasRenta 
        case "2020":
            rentaTotal = 700 * diasRenta 
        case "2021":
            rentaTotal = 750 * diasRenta
        
    if edad >= 15 and edad <= 18:
        seguroMenor = rentaTotal * 0.8 
        imprimirCotizacion(licencia, edad, rentaTotal, seguroMenor) 
    else:
        imprimirCotizacion(licencia, edad, rentaTotal) 
        
IngresaInformacion()