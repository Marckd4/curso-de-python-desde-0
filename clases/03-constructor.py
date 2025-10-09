class Perro: 
    def __init__(selt, nombre, edad):
        selt.nombre = nombre
        selt.edad = edad
        
    def habla(selt):
        print(f"{selt.nombre} dice: guau!")
        
mi_perro =Perro("dog", 1)
mi_perro.habla()