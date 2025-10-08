# and True = True  - or  True = False -not  es negar 

gas = True 
encendido = True
edad = 18

# if gas and encendido:
#     print("Puedes avanzar")

# if gas and encendido and edad >17 :
#     print("Puedes avanzar")

if gas and (encendido or edad > 17):
    print("Puedes avanzar")
