import os

def init():
    print(' --Administrador de archivos-- ')
    option = input(' Por favor, escribe la letra C para crear o E para eliminar un archivo: ')
    while(option.lower() != 'c' and option.lower() != 'e'):
            option = input(' ** La opción ingresada no es válida ** Por favor, escribe la letra C para crear o E para eliminar un archivo: ')
    if(option.lower() == 'c') : 
        route = input(' Correcto, crearemos el archivo. Podes indicarnos una ruta ahora o el archivo se creará sobre la ruta actual: ')
        if(route == '') :  route = os.getcwd() + "\\" #obtenemos la ruta actual 
        if(os.path.isdir(route)) : 
            type = input(' Indique el tipo, utilizando la letra A si es archivo y C para carpeta: ')
            while(type.lower() != 'c' and type.lower() != 'a'):
                type = input(' ** El tipo ingresado no es válido ** Indique el tipo, utilizando la letra A si es archivo y C para carpeta: ')
            if(type.lower() == 'a') :
                archive = input(' Diganos el nombre que desea colocarle al archivo: ')
                archiveHandler = open(route+archive, 'w')
                archiveHandler.close()
                print(' El archivo', archive, ' fué creado con exito')
            else : 
                file = input(' Diganos el nombre que desea colocarle al su carpeta: ')
                os.mkdir(route+file)
                print(' Su carpeta', file, ' fué creada con exito')
    else :
        route = input(' Correcto, eliminaremos el archivo. Podes indicarnos una ruta ahora o el archivo se tratará sobre la ruta actual: ')
        if(route == '') :  route = os.getcwd() + "\\" #obtenemos la ruta actual 
        delete = input (' Indique el nombre de la carpeta o archivo que desea eliminar: ')
        if(os.path.isfile(route+delete)) :
            os.remove(route+delete)
            print(' El elemento ', delete, ' se eliminó correctamente ')
        elif(os.path.isdir(route+delete)) :
            os.rmdir(route+delete)
            print(' El elemento ', delete, ' se eliminó correctamente ')

init()



