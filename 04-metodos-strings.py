
# upper es metodos que son funciones de un objeto
# lower es metodo en minusculas 
# capitalize toma el primer caracter y lo trasnforma en mayuscula
# title coloca con mayuscalas la primera palabra y el segundo trozo de parrafo y lo convierte en mayuscula el inicio
# strip remueve los espacios en blancos al comienzo - iz y derecha 
# find extrae la cadena de caracteres(indice)
# replace remplaza a cararcteres de la frace o palabras
# (in) es encontrar o mostrar boolean True False (dentro de una variable )
# not - in - animal busca si no se encuentra dentro de la variable
animal = "gatos felices"

print(animal.upper())
print(animal.lower())
print(animal.capitalize())
#print(animal.strip().capitalize()) se puede concatenear los metodos 
print(animal.title())
print(animal.strip())
print(animal.rstrip())#espacio a la derecha 
print(animal.lstrip())# espacio a la 
print(animal.find("gatos"))
print(animal.replace("gatos", "cat"))
print("gatos" in animal )
print("gatos" not in animal)