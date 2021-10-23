from conectar import conectar as con


while True:
    opcion = int(input("Ingresar opcion: "))

    if opcion == 1:
        login = input("ingrsar correo: ")
        contraseña = input("Ingresar contraseña: ")
        con(login, contraseña)

        