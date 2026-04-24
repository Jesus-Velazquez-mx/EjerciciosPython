from Libro import Libro, Revista

libro1 = Libro()
libro1.nombre = "Sombras"
libro1.paginas = 200
libro1.setColor("Rojo")
libro2 = Libro("Sin teclado", 100, "Verde")
Revista1 = Revista("Cosmopolitan", 50, "Blanca", 12488439292, "2024")

print(libro1.__str__())
print(libro2.__str__())
print(Revista1.__str__())