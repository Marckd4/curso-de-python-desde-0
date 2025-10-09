#lista =[1,2,3,4,5,6] # fifo

#lista =list(range(100_000_000))

# deque es una clase


from collections import deque

fila = deque([1,2])
# fila.append(3)
# fila.append(4)
# fila.append(5)

print(fila)

fila.popleft()# elimina de la izquierda
print(fila)

if not fila:
    print("fila vacia")

