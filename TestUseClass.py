from TestClass import Libro

book = Libro()
book.nombre = "El libro x"
book.hojas = 210
book.tamaño = "Mediano"
book.setColor("Azul")

print(book.__str__())