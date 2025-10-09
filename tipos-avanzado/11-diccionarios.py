punto = {"x" :25, "y" :50 }

# solo string en la llave como inicio 

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)


print(punto.get("x"))
print(punto.get("lala", 97))

# eliminar alguna lleve por su valor 

del punto ["x"]
del punto ["y"]

print(punto)

punto ["X"] = 25

for valor in punto:
    print (valor, punto[valor])
    
for valor in punto.items():
    print(valor)
    
for llave in punto.items():
    print(llave, valor)
    
# diccionario

usuarios =[
    
    {"id": 1, "nombre": "caja"},
    {"id": 2, "nombre": "unidad"},
    {"id": 3, "nombre": "pack"},
]

for usuario in usuarios:
    print(usuario["nombre"])