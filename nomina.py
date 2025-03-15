##us1/crear registro
users = [[],[]]

def createUser():
    user = []
    id = int(input("Ingrese su documento de identidad"))
    user.append(id)
    user_name = input("Ingrese su nombre")
    user.append(user_name)
    phone = input("Ingrese su numero de telefono")
    user.append(phone)
    user_last_name = input("Ingrese su correo electronico.")
    user.append(user_last_name)
    user_password = input("Ingrese su contraseña")
    user.append(user_password)
    user.append(user)

createUser()
createUser()
createUser()

print(users)

    
