class Libro:
    def __init__(self):
        self.nombre = None
        self.hojas = None
        self.tamaño = None
        self.__color = None
    
    def setColor(self, clr):
        self.__color = clr

    def __str__(self) -> str:
        return("Libro " + str(self.nombre) + " de tamaño " + str(self.tamaño) + " y de color " + str(self.__color))   