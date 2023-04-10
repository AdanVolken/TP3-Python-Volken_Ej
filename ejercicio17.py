'''
Usar la función webbroser para mostrar una página html que tenga el título
Programación 2 y muestre una lista desordenada con los siguientes ítems:
Condicionales
Bucles
Listas
Funciones
Agregar enlace para ingresa a cada una de las opciones
'''


import webbrowser

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programacion 2</title>
</head>
<body>
    <h1>Programacion 2</h1>
    <ul>
       <li><a href="https://www.w3schools.com/python/python_conditions.asp">Condicionales</a></li>
        <li><a href="https://tutorial.recursospython.com/bucles/">Bucles</a></li>
        <li><a href="https://www.w3schools.com/python/python_lists.asp">Listas</a></li>
        <li><a href="https://www.w3schools.com/python/python_functions.asp">Funciones</a></li>
    </ul>
</body>
</html>
"""

with open('ejercicio 17.html', 'w') as p:    
    p.write(html)

try:
    webbrowser.open_new_tab('ejercicio 17.html')
except webbrowser.Error as e:
    print(f'Error: {e}')
