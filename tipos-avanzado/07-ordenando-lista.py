numeros = [2, 5, 55, 66, 6, 8, 14, 44]

#numeros.sort()# lista ordenada
# sorted (numero) nueva lista 

numeros.sort(reverse=True) # lista ordenada de orden desendente
print(numeros)

#usuarios = [[1, "gatos"], [3, "leones"], [2,"perro"]]
usuarios = [["gatos", 1], ["leones", 3], ["perro", 2]]

# def ordena(elemento):
#     return elemento[1]

#usuarios.sort(key=ordena)
usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)