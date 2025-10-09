
# apilamineto de algunos objeto # lifo 
# metodo de pop es eliminar el ultimo elemento

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)

print(pila)

ultimo_elemento= pila.pop()
print(ultimo_elemento)

if not pila:
    print("pila vacia")