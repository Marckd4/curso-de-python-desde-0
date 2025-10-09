class Perro:
    patas = 4 
    def __init__(selt, nombre, edad):
        selt.nombre = nombre
        selt.edad = edad
        
    def habla(selt):
        print(f"{selt.nombre} dice: guau!")
        
mi_perro =Perro("dog", 1)
print(Perro.patas)
