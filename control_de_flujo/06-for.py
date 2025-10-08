# for iterar una lista de elenemto 

buscar = 15

for numero in range(5):
    print(numero)
    if numero == buscar:
       print("encontrado", buscar)
       break
else:
    print("no encontre el numero")
       