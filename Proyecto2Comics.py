# =========================================================================================================================
#   >>> PROYECTO 2:
# =========================================================================================================================
#   Librerias:

import sys                                                               # oredenar lista de lista segun uno de sus parametros
from operator import itemgetter                                          # ?
from time import sleep                                                   # Controlar los tiempos de muestra
import colorama                                                          # colores de letra e imprenta elegante

inventario = []
modulo_serial = []
archivo = open("comics.txt") # txt
for i in archivo:
    linea = str(archivo.readline())
    aux = []
    for j in linea:
        if j != "~":
            pass
    inventario.append(aux)

archivo.close()

print(inventario)
exit()

# =========================================================================================================================
#   listas necesarias

inventario =[["jose",26303183,100,5,True], ["chao pescao",87456123,50,3,True],["jose volvio", 26303186, 450, 6, True]]                        # inventario general
numSerie=[[0,26303183],[1,87456123]]                                                  # numero de serie y posicion relativa
palabras =[[1, "chao"], [0, "jose"], [2, "jose"], [1, "pescao"], [2,"volvio"]]                                        # palabras con posicion relativa
count = [0]
# =========================================================================================================================
#   Funciones:
# -------------------------------------------------------------------------------------------------------------------------
def menu(count):                                    # Mostrar Menu principal con las opciones posibles a ingresar por el usuario
    
    if count[0] == 0:
        print("""
    >> Bienvenido a la tienda de comics, porfavor elije una opcion:""")
    else:
        if (count[0] % 2) == 0: 
            print("\n    >> Elija una de las opciones para interactuar con la tienda:")
        else:
            print("\n    >> Bienvenido otra vez, ¿Que accion desea realizar ahora?:")
    count[0] += 1
    sleep(0.56)
    print('''
        1. Buscar Historieta
        2. Comprar Historieta
        3. Reabastecer Inventario
        4. Eliminar historieta
        5. Compactar Inventario

        0. Salir del Programa
    ''')

    return count
 
# -------------------------------------------------------------------------------------------------------------------------
def agregarH(inventario, numSerie, palabras):               # crear la lista que queremos agregar (faltan las validaciones)

    registrable = True
    while(True): # Bucle de Registro de nombre
        try:

            nombre = input("Ingrese el Nombre de la Historieta (MAX 40 Caracteres): ") # Ingresar el nombre de la historieta

            # Verificar que el comic sea acto de entrar al sistema :

            if len(nombre) == 0 or len(nombre) > 40: # Tiene una cantidad de caracteres aceptable en el nombre
                print(" >> Nombre invalido")
                registrable = False

            print(len(inventario)) 

            if len(inventario) != 0:
                for i in range(0, len(inventario)): # No esta ya registrada con anterioridad al sistema 
                    print(f"{i} lista  {inventario[i][0]}")
                    if nombre == inventario[i][0]: # Se encontro una coincidencia
                        print(" >> Ya hay registrado un comic bajo ese nombre.")
                        registrable = False
                        break

            if registrable == False: # Se detecto que ya habia en la lista un comic con ese nombre

                print(" >> ¿Desea volver a intentar registrar la historieta?:")

                while(True): # Desea continuar el registro?
                    try:
                        question_repeat = int(input(" 1 - Si / 2  - No "))
                        if question_repeat == 1:
                            registrable = True
                            break
                        elif question_repeat == 2:
                            break
                        else:
                            print(" >> Comando invalido, intente nuevamente")
                    except ValueError:
                        print(" \n>> Error de comando, solo se aceptan numeros\n")
                    except:
                        print(" \n>> Error desconocido\n")

                if registrable == True:
                    continue
                else:
                    break
            else:
                break
        except ValueError:
            print(" \n>> Error de comando\n")
        except:
            print(" \n>> Error desconocido\n")

    while(True): # Bucle de registro de serial
        try:    
            serial = int(input("Ingrese el serial de la Historieta (8 Digitos): ")) # Ingresar el serial de la historieta
            if len(str(serial)) == 8 and serial >= 0:
                print(" >> Serial aceptado")
                break
            else:
                print(" >> Los seriales deben llevar 8 digitos, porfavor intente denuevo")

        except ValueError:
            print(" \n>> Error de comando, solo se aceptan numeros\n")
        except:
            print(" \n>> Error desconocido\n")    

    while(True): # Bucle registro de precio
        try:    

            precio = int(input("Ingrese el Precio de Venta (MAX 3 Digitos): "))

            if len(str(precio)) <= 3 and precio > 0:
                print(" >> Precio aceptado")
                break
            else:
                print(" >> Los costos deben tener un tamaño maximo de 3 digitos y no pueden ser menores a 1$, porfavor intente denuevo")


        except ValueError:
            print(" \n>> Error de comando, solo se aceptan numeros\n")
        except:
            print(" \n>> Error desconocido\n")    

    while(True): # Bucle de registro de cantidad
        try:     

            num = int(input("ingrese el numero de historietas que se agregan al inventario (MAX 2 Digitos) : "))

            if len(str(num)) <= 2 and num > 0:
                print(" >> Numero aceptado")
                
            else:
                print(" >> En el inventario caben hasta 99 comics, por favor intente de nuevo")
                continue

            agregar = [nombre,serial,precio,num] 
            agregar.append(True)

            # agregamos la lista introducida al inventario general 

            inventario.append(agregar)

            print(inventario)

            # agregamos  la lista introducida a la lista numSerie

            for i in range(len(inventario)):
                numserie = inventario[i][1]
                poscRelativa = i
                temporal = [poscRelativa,numserie]
                numSerie.append(temporal)
                print(numSerie)
            
            # agregamos la lista introducida a lista palabras 
            for i in range(len(inventario)):
                nombre = inventario[i][0]
                prelativa = i
                nombre = str(nombre)
                splits = [prelativa, nombre]
                palabras.append(splits)
                print(palabras)
                
            break

        except ValueError:
            print(" \n>> Error de comando, solo se aceptan numeros\n")
        except:
            print(" \n>> Error desconocido\n")


    return inventario, numSerie, palabras
# -------------------------------------------------------------------------------------------------------------------------
def ordenar(lista,posicion): # ordenar cualquier lista segun el parametro que pasemos(podemos usar esto o tenemos que hacer nuesto propio algoritmo?)
    
    ordenada = sorted(lista, key=itemgetter(posicion))
    print(ordenada)
    return ordenada
# -------------------------------------------------------------------------------------------------------------------------    
def imprimirBusqueda():                                           # Mostrar las opciones con la cual se realiza la busqueda

    # Preguntar mediante que metodo desea buscar la historieta

    print(''' 
    Buscar mediante:

    1. Serial
    2. Una o Dos palabras del titulo

    0. Volver atras\n
    ''')
# -------------------------------------------------------------------------------------------------------------------------
def buscar(code):                                                                # Buscar una historieta dentro del sistema

    seguirBusqueda = True
    
    # Preguntar mediante que metodo desea buscar la historieta

    imprimirBusqueda()

    # Operar algoritmo de busqueda:

    while(True): # Bucle de seleccion de un metodo
        #try:
            respuesta_2 = int(input("==> ")) # Ingresar una opcion
            # Opciones: 

            if respuesta_2 == 1: # Buscar por serial
                print(" >> Seleccionado, buscar por serial")
                x = buscar_serial(numSerie)
                if code == 1:
                    print(" >> ¿Desea buscar otra? 1 - Si | 2 - No \n")
                    while(True):
                        try:
                            seguir = int(input("  ==> "))
                            if  seguir == 1:
                                imprimirBusqueda() # Repite impresion para continuar trabajando
                                break
                            elif seguir == 2:
                                seguirBusqueda = False
                                break
                            else:
                                print("Seleccion equivocada")
                        except:
                            print("Comando invalido, seleccione un numero")
                    if seguirBusqueda == False:
                        break
                elif code == 2:  
                    break

            elif respuesta_2 == 2: # Buscar por palabras 
                print(" >> Seleccionado, buscar palabras:\n " + "-"*50 +"\n >> ¿Desea usar una o 2 palabras?: ")
                while(True):
                    target = input(" >>> ")
                    if target.isnumeric():
                        target = int(target)
                        if target == 1:
                            x = buscar_name(palabras, code)
                            break
                        elif target == 2:
                            x = buscar_name_segundo(palabras, code)
                            break
                        else:
                            if(target < 0):
                                print("Error de logica numerica")
                            elif(target >= 10):
                                print("Demasiadas palabras para el sistema")
                            else:
                                print("Cantidad de palabras no valida")
                            print("Intente nuevamente")
                    else:
                        print("Por favor introduzca un caracter numerico en este campo.")
                break
            elif respuesta_2 == 0: # No queria entrar a esta opcion, deseo volver al menu para seleccionar la opcion deseada
                x = None
                break
            else: # Validar que si es un numero no contemplado en la lista intente nuevamente seleccionar
                print("Su selección no fue valida, intente nuevamente")
        #except:
        #    print("Comando invalido, seleccione un numero")
    return x 
# -------------------------------------------------------------------------------------------------------------------------        
def buscar_serial(numSerie):                                            # Busca por el serial en la tabla extra una libreta

    buscar_serial = int(input("\n >> Introduzca el serial de la Historieta que desea buscar: ")) # Ingresar serial de la historieta

    # Variables de control:
    
    inicio = 0
    final = len(numSerie)-1
    encontrado = False
    x = None

    # Busqueda binaria:

    while(inicio <= final):
        mitad = (inicio + ((final - inicio)//2))
        valor_mitad = numSerie[mitad][1]
        if valor_mitad == buscar_serial:
            relativo = numSerie[mitad][0] # 26303183
            print("> " + "-"*95 + "<")
            x = imprimir(relativo)
            print("> " + "-"*95 + "<")
            encontrado = True
            break
        elif valor_mitad > buscar_serial:
            final = mitad -1
        else:
            inicio = mitad +1
    if(encontrado == True):
        return [x, relativo]
    else:
        print("No hay ejemplares disponibles.")
        return None
# -------------------------------------------------------------------------------------------------------------------------
def buscar_name(palabras, code):

    buscar_palabra = input("\n >> Introdusca la palabra que desea buscar: ")
    # Variables de control:

    inicio = 0
    final = len(palabras)-1
    encontrado = False
    x = []
    v = []

    # Busqueda Binaria:

    while(inicio <= final):
        mitad = (inicio + ((final - inicio)//2))
        valor_mitad = palabras[mitad][1]
        if valor_mitad in buscar_palabra:
            relativo = palabras[mitad][0] # 26303183
            v.append(relativo)
            print("> " + "-"*95 + "<")
            x.append(imprimir(relativo))
            print("> " + "-"*95 + "<")
            encontrado = True
            countPositivo = 1
            countNegativo = 1
            while(True):
                if palabras[mitad-countNegativo][1] in buscar_palabra:
                    relativo = palabras[mitad-countNegativo][0]
                    v.append(relativo)
                    x.append(imprimir(relativo))
                    print("> " + "-"*95 + "<")
                    countNegativo += 1
                else:
                    break
            if len(palabras) > (mitad + 1):
                while(True):
                    if palabras[mitad+countPositivo][1] in buscar_palabra:
                        relativo = palabras[mitad+countPositivo][0]
                        v.append(relativo)
                        x.append(imprimir(relativo))
                        print("> " + "-"*95 + "<")
                        countPositivo += 1
                    else:
                        break
            break
        elif valor_mitad > buscar_palabra:
            final = mitad -1
        else:
            inicio = mitad +1
    if(encontrado == True):
        print("Encontrada")
        y = []
        if code >= 2 and len(x) > 1:
            if code == 2:
                print("Seleccione cual de los resultados desea comprar: ")
            elif code == 3:
                print("Seleccione cual de los resultados desea borrar: ")
            for i in range(0, len(x)):
                print(f"> -- {i+1} --" + "-"*90 + "-- <" + f'\n> N° de Serial:{x[i][1]} | Nombre: {x[i][0]} | Precio: {x[i][2]} | Ejemplares disponibles: {x[i][3]}')
            print(f"> -- {i+1} --" + "-"*90 + "-- <")
            
            while(True):
                try:    
                    z = int(input( " ==> " ))
                    if z <= len(x) and z > 0: 
                        y = x[z-1]
                        relativo = v[z-1]
                        break
                    else:
                        print(" >> Error A")
                except:
                    print(" >> Error B")
                
        else:
            y = x[0]
            
        return [y, relativo]

    else:
        print("No hay ejemplares disponibles.")
        return None
# -------------------------------------------------------------------------------------------------------------------------
def buscar_name_segundo(palabras, code):

    buscar_palabra1 = input("\n >> Introdusca la palabra 1 que desea buscar: ")
    buscar_palabra2 = input(" >> Introdusca la palabra 2 que desea buscar: ")
    # Variables de control:

    inicio = 0
    final = len(palabras)-1
    encontrado = False
    x = []
    w = []
    u = []
    v = []

    # ---------------------------------------------------------------------------------------------------
    # Busqueda Binaria:
    # ---------------------------------------------------------------------------------------------------
    # Parte 1:
    # ---------------------------------------------------------------------------------------------------
    while(inicio <= final):
        mitad = (inicio + ((final - inicio)//2))
        valor_mitad = palabras[mitad][1]
        if valor_mitad in buscar_palabra1:
            relativo = palabras[mitad][0] # 26303183
            v.append(relativo)
            print("> " + "-"*95 + "<")
            x.append(imprimir(relativo))
            print("> " + "-"*95 + "<")
            encontrado = True
            countPositivo = 1
            countNegativo = 1
            while(True):
                if palabras[mitad-countNegativo][1] in buscar_palabra1:
                    relativo = palabras[mitad-countNegativo][0]
                    v.append(relativo)
                    x.append(imprimir(relativo))
                    print("> " + "-"*95 + "<")
                    countNegativo += 1
                else:
                    break
            if len(palabras) > (mitad + 1):
                while(True):
                    if palabras[mitad+countPositivo][1] in buscar_palabra1:
                        relativo = palabras[mitad+countPositivo][0]
                        v.append(relativo)
                        x.append(imprimir(relativo))
                        print("> " + "-"*95 + "<")
                        countPositivo += 1
                    else:
                        break
            break
        elif valor_mitad > buscar_palabra1:
            final = mitad -1
        else:
            inicio = mitad +1
    # ---------------------------------------------------------------------------------------------------
    # Parte 2:
    # ---------------------------------------------------------------------------------------------------
    while(inicio <= final):
        mitad = (inicio + ((final - inicio)//2))
        valor_mitad = palabras[mitad][1]
        if valor_mitad in buscar_palabra2:
            relativo = palabras[mitad][0] # 26303183
            v.append(relativo)
            w.append(imprimir(relativo))
            print("> " + "-"*95 + "<")
            encontrado = True
            countPositivo = 1
            countNegativo = 1
            while(True):
                if palabras[mitad-countNegativo][1] in buscar_palabra2:
                    relativo = palabras[mitad-countNegativo][0]
                    v.append(relativo)
                    w.append(imprimir(relativo))
                    print("> " + "-"*95 + "<")
                    countNegativo += 1
                else:
                    break
            if len(palabras) > (mitad + 1):
                while(True):
                    if palabras[mitad+countPositivo][1] in buscar_palabra2:
                        relativo = palabras[mitad+countPositivo][0]
                        v.append(relativo)
                        w.append(imprimir(relativo))
                        print("> " + "-"*95 + "<")
                        countPositivo += 1
                    else:
                        break
            break
        elif valor_mitad > buscar_palabra2:
            final = mitad -1
        else:
            inicio = mitad +1
    # ---------------------------------------------------------------------------------------------------
    # Resolucion:
    # ---------------------------------------------------------------------------------------------------
    if(encontrado == True):
        print("Encontrada")
        for j in range(0, len(x)):
            u.append(x[j])
        for k in range(0, len(w)):
            u.append(w[k])   
        y = []
        if code >= 2 and len(u) > 1:
            if code == 2:
                print("Seleccione cual de los resultados desea comprar: ")
            elif code == 3:
                print("Seleccione cual de los resultados desea borrar: ")
            for i in range(0, len(u)):
                print(f"> -- {i+1} --" + "-"*90 + "-- <" + f'\n> N° de Serial:{u[i][1]} | Nombre: {u[i][0]} | Precio: {u[i][2]} | Ejemplares disponibles: {u[i][3]}')
            print(f"> -- ○ --" + "-"*90 + "-- <")
            
            while(True):
                try:    
                    z = int(input( " ==> " ))
                    if z <= len(u) and z > 0: 
                        y = u[z-1]
                        relativo =  v[z-1]
                        break
                    else:
                        print(" >> Error A")
                except:
                    print(" >> Error B")
                
        else:
            y = x[0]
            
        return [y, relativo]

    else:
        print("No hay ejemplares disponibles.")
        return None
# -------------------------------------------------------------------------------------------------------------------------

def imprimir (relativo):                 # impirme todos los valores de la historieta con ese numero relativo en inventario

    nombre = inventario[relativo][0]     # Nombre del comic
    serial= inventario[relativo][1]      # Numero de serial
    precio= inventario [relativo][2]     # Costo del comic
    ejemplares= inventario[relativo][3]  # Cuantos de este modelo quedan
    
    print(f'> N° de Serial:{serial} | Nombre: {nombre} | Precio: {precio} | Ejemplares disponibles: {ejemplares}') # Imprimir datos ordenados

    return [nombre, serial, precio, ejemplares] # Para operar
# -------------------------------------------------------------------------------------------------------------------------
def comprar(inventario):       
    #count = 1                                                                             # Adquirir una historieta
    #for i in range(0, len(inventario)):
    #    if inventario[i][4] == True:
    #        print(f"> -- {count} --" + "-"*90 + "-- <")
    #        imprimir(i)
    #        count += 1
    #print(f"> -- ○ --" + "-"*90 + "-- <")
    #print("> Cual desea llevar?\n")

    while(True):
        print("Como desea buscar la historieta a comprar")
        x = buscar(3)
        if x == None:
            break
        print("\nRevista:\n\n" + f"Nombre: {x[0][0]}\nSerie: {x[0][1]}\nPrecio: {x[0][2]}\nEjemplares Restantes: {x[0][3]}\n")
        
        # Pedir ejemplares:

        print("¿Cuantos ejemplares deseas llevar?\n")
        while(True):
            try:
                cantidad = int(input(" ==> "))
                if cantidad <= 0:
                    print("En este departamento Debe ordenar una cantidad a llevar, no a entregar")
                    continue
                elif cantidad > x[0][3]:
                    print("No disponemos de esa cantidad de copias, intentelo nuevamente")
                    continue
                else:
                    print("Procesando operacion:\n")
                    sleep(1)
                    cash = cantidad * x[0][2]
                    factura = f"""
                    =========================================
                       >>>         FACTURACION:        <<<
                    -----------------------------------------
                      Comics seleccionado:  {x[0][0]}.
                      Comics comprados:     {cantidad}.
                      Serial:               {x[0][1]}.
                      Coste unidad:         {x[0][2]}$
                      Coste total:          {cash}$
                    -----------------------------------------
                        >>> TOTAL: {cash}
                    -----------------------------------------   
                    """
                    print(factura)
                    sleep(1)

                    inventario[x[1]][3] -= cantidad

                    print(" >> Compra procesada, que tenga un excelente dia.")

                    break
            except:
                print("Error de compra")
        break
# -------------------------------------------------------------------------------------------------------------------------
def eliminado():               # Pone en apunte que debe sacar del sistema comic que eliminara definitivamente proximamente
    
    print("Como desea buscar la historieta a sacar del sistema:\n")
    x = buscar(3)
    print("="*98 + "\nRevista:\n\n" + f"Nombre: {x[0][0]}\nSerie: {x[0][1]}\nPrecio: {x[0][2]}\nEjemplares Restantes: {x[0][3]}\n" + "-"*98)
    sleep(1)
    print("""
    > Seguro desea eliminar este elemento del catalogo:

        1 - Si 
        2 - No
    """)

    while(True):
        try:
            delete = int(input( "   > >>> "))
            sleep(1)
            if delete == 1:
                inventario[x[1]][4] = False
                print("\n  >> Comic retirado de circulacion correctamente.\n" + "-"*98)
                break
            elif delete == 2:
                print("\n  >> Entendido. Cancelando eliminacion.\n" + "-"*98)
                break
            else:
                print("Opcion no valida")
        except:
            print("Error de comando de seleccion no valido.")    
# -------------------------------------------------------------------------------------------------------------------------
def compact():                                                                               # Proceso de eliminacion final 
    temp = 0
    print("\n >> Porfavor espere, esto podria tardar unos segundos...\n")
    sleep(2)
    n = len(inventario)
    for m in range(0, n):
        for i in range(0, len(inventario)):
            if inventario[i][4] == False:
                x = inventario[i][1]
                print(f"Desechando a: {x}")
                for j in range(0, len(numSerie)-1):
                    if numSerie[j][1] == x:
                        temp = numSerie[j][0]
                        numSerie.pop(j)
                y = inventario[0]
                for k in range(0, len(palabras)-1):
                    if palabras[k][1] in y and palabras[k][0] == temp:
                        palabras.pop(k)
                inventario.pop(i)
                break

    print(" >> Base de datos compactada exitosamente.\n")

    #print(inventario)
    #print(numSerie)
    #print(palabras)
    sleep(0.2)
    print("-"*120 + "\n")
    sleep(1)
# -------------------------------------------------------------------------------------------------------------------------
def main():                                                                                  # Funcion principal del codigo

    while True: # Bucle principal

        #try:

            menu(count) # llamar Muestra del menu de opciones:
            
            # Pedir al usuario que seleccione una opcion:
            sleep(0.6)
            respuesta = int(input( "    >>> SELECCION: ")) # Ingresar un numero del 0 al 6
            print("\n"+ "-"*120)
            if respuesta == 1:
                buscar(1)

            elif respuesta == 2:
                print("> Comprar una Historieta:")
                comprar(inventario)

            elif respuesta == 3:
                agregarH(inventario, numSerie, palabras)

            elif respuesta == 4:
                print("eliminar historieta:")
                eliminado()

            elif respuesta == 5:
                print("\nCompatar inventario:")
                compact()

            elif respuesta == 0:
                sleep(0.8)
                print("\n >> Hasta la proxima usuario. \n")
                sleep(0.8)
                break
                #sys.exit()

            else:
                print (" \n>> Su seleccion no fue valida, intente de nuevo por favor:\n")

        #except ValueError:
        #    print(" \n>> Error de comando, solo se aceptan numeros\n")
        #except:
        #    print(" \n>> Error desconocido\n")

# =========================================================================================================================
sleep(0.5)                                                                                                         # Suspenso
print("\n>> "+"="*114 + " <<")
sleep(0.6)
print(" "*48 + "Welcome to Comic-Land:")
sleep(0.6)
print(">> "+"="*114 + " <<")     # Un membrete decorativo
sleep(0.7)
main()                                                                                     # Empezar ejecucion del programa
# =========================================================================================================================
# Programar, es un arte, asi como el dibujar