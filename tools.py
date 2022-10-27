#extract_info, clear_info, paste_info

from operator import index
import os
import csv

def extract_info():
    #Retorna una lista con sublistas de año-mes-dia-monto-numerodeliquidacion
    try:
        with open(f"Archivo_a_limpiar.csv", "r") as archivoL:
            lector=csv.reader(archivoL, delimiter=",")
            
            lineas_copiadas=[]
            for linea in lector:
                lineas_copiadas += [linea]
                #diacopiado=Delistastr(listadia, "")
                
            return lineas_copiadas
    except FileNotFoundError as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\nEl arcivo 'Liquidación diaria.csv' no fue encontrado")
        print("Depositar el archivo 'Liquidación diaria.csv' dentro de la carpeta 'config' del programa")
        print (e)
        print("--------------------------------------")
        input("Presione ENTER para continuar\n")

    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        archivoL.close()


def clear_info(info:list, to_eliminate:str, to_insert=''):
    new_info =[]
    
    for line in info:
        new_line =[]
        for field in line:
            if to_eliminate in field:

                field = field.replace(to_eliminate, to_insert)
                
                field = float(field.replace(',', '.'))/100
                
                field = f'{field:.4f}'.replace('.', ',')
                
                new_line += [field]
            
            else:
                new_line += [field]
        new_info += [new_line]
        
    return new_info

def paste_info(texto, m='w'):            #Escribe en la base de datos lo que le pasas en lugar de "texto"
    """
     _summary_
     se le pasa un texto y segun el metodo indicado:
     Elimina el contenido previo de la DB
     Suma el contenido al lo que previamente contenia la DB
     
     m:
     'a', 'A'= Agregar al archivo existente
     'w', 'W'= Escribir un nuevo archivo
     Args:
     texto ([STR]): Texto dentro de una lista, ocupara un renglon en el archivo csv
     m (STR): Letra que espesifica el metodo a utilizar en la apertura del archivo
    """

    try:
        if os.name == "nt" or os.name=="dos":
            chequeoos='\\'
            
        elif os.name =="posix":
            chequeoos='/'

        if m == False or m == "a" or m == "A":
            metodo="a"
        
        elif m == "w" or m == "W":
            metodo="w"

        with open(f"Archivo_limpio.csv", f"{metodo}", newline="")as archivoacsv:
            escritor=csv.writer(archivoacsv, delimiter=";")
            escritor.writerows(texto)

    except FileNotFoundError:
        print(f"\tError!!\nError de tipo:FileNotFoundError\nEl programa no detecta la carpeta config.\nDe no existir la carpeta config dentro de la carpeta raiz del programa por favor: Crearla y reiniciar el programa \n--------------------------------------")
        input("Presione ENTER para continuar\n")


    except Exception as e:
        print(f"\tError!!\nError de tipo:{type(e).__name__}\n{e}\n--------------------------------------")
        input("Presione ENTER para continuar\n")

    finally:
        archivoacsv.close()


