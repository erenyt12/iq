from iqoptionapi.stable_api  import IQ_Option
import time

# Funcion conectar
def conectar(login, contraseña):
    """ Ingrear correo y contraseña para conectar al broker """
    api = IQ_Option(login, contraseña)

    while True:
        if api.check_connect() == False:
            print("Error al conectar")
        else : 
            print("Conectado correctamente")
            break

        time.sleep(1) 