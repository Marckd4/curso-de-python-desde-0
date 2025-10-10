class Perro:
    def __init__(selt, nombre, edad):
        selt.__nombre = nombre
        selt.edad = edad
        
 
        
    def habla(self):
        print(f"{self.__nombre} dice: guau!")
        
        
    @classmethod
    def factory(cls):
        return cls("feliz",4)
        
perro1 = Perro.factory()
perro1.habla()