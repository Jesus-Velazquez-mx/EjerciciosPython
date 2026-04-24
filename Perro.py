class Perro:
    familia = "canina"    
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def sonido(self):
        print("Guau guau") 

    def __str__(self) -> str:
        print("Nombre: " + self.nombre + "\n Raza: " + self.raza + "\n Edad: " + str(self.edad))
        
Perrito = Perro("Coffe", "Chihuahua", 2)
Perrito2 = Perro("Panfilo", "Chihuahua", 1)
print(Perrito.__str__())
print(Perrito2.__str__())
    
    
    


    