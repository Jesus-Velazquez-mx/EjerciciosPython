class Libro:
    def __init__(self, nombre = None, pags = None, clr = None):
        self.nombre = nombre
        self.paginas = pags
        self.__color = clr
    
    def setColor(self, clr):
        self.__color = clr

    def __str__(self) -> str:
        return("El libro " + str(self.nombre) + " tiene " + str(self.paginas) + " y es color " + str(self.__color))

class librox:
    def __init__(self):
        self.nombre = None
        self.paginas = None
        self.__color = None

class Revista(Libro):
    def __init__(self, nombre=None, pags=None, clr=None, pID=None, aP=None):
        super().__init__(nombre, pags, clr)
        self.publicacionID = pID
        self.AñoPublicacion =aP

    def __str__(self) -> str:
        return "La revista {} tiene {} paginas y fue publicada en el año{} ".format(self.nombre,self.paginas, self.AñoPublicacion )