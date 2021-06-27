# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    try:
        csvfile = open(archivo, 'r')
        stock = list(csv.DictReader(csvfile))
        csvfile.close()
    except:
        print(f'Error al abrir el archivo {archivo}.')
    
    columna = 'tornillos'
    cant_tornillos = 0
    for i in range(len(stock)):
        cant_tornillos += int(stock[i][columna])
    print(f'Cantidad total de {columna}: {cant_tornillos}')
        

def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    try:
        csvfile2 = open(archivo, 'r')
        propiedades = list(csv.DictReader(csvfile2))
        csvfile2.close()
    except:
        print(f'Error al abrir el archivo {archivo}.')
    columna = 'ambientes'
    columna2 = 'titulo'
    dos_ambientes = 0
    tres_ambientes = 0
    for i in range(len(propiedades)):
        try:
            if int(propiedades[i][columna]) == 2:
                dos_ambientes += 1
            elif int(propiedades[i][columna]) == 3:
                tres_ambientes += 1
        except:
            print(f'Error en {columna} de la propiedad {propiedades[i][columna2]}.')
    print('Cantidad de propiedades de 2 ambientes: ', dos_ambientes)
    print('Cantidad de propiedades de 3 ambientes: ', tres_ambientes)
        



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
