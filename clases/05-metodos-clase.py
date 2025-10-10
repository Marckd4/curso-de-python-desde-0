class Perro:
    patas = 4 
    def __init__(selt, nombre, edad):
        selt.nombre = nombre
        selt.edad = edad
        
    @classmethod 
        
    def habla(cls):
        print( "guau!")
        
    @classmethod
    def factory(cls):
        return cls("feliz con el botin",4)
        
Perro.habla()
perro1 = Perro("Feliz", 2)
perro2 = Perro("juan", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)