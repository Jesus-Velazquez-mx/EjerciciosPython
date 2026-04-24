class Perro:
    def __init__(self, nombre,raza):
        self.nombre = nombre
        self.raza = raza
    
    def ladrar(self):
        print("Guau!")

perro = Perro("Niebla", "Mastín")
print(perro.nombre)
print(perro.raza)
perro.ladrar()