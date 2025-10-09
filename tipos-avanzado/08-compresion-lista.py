usuarios = [
    ["gatos", 1],
    ["leones", 3], 
    ["perro", 2]
    
]


#  for literar el listado 

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# nombres = [expresion for item in items]
#nombres = [usuario [0] for usuario in usuarios]


# filtra

nombres = [usuario for usuario in usuarios if usuario [1] > 2 ]
print(nombres)


# nombres = list(map(lambda usuario: usuario[0]))
# menosUsuarios = list(filter(lambda usuario[1] > 2))