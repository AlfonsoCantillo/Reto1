import os
import msvcrt
import menuGestion
import menuPrincipal

#Funcion para mostrar el submenú "Análisis de resultados"
def mostrarMenu(listaExperimentos):
  #Limpiar la pantalla
  os.system("cls")  
  #Inicializar un ciclo para interactuar con el submenú  
  while True: 
    print("Menú de opciones / Análisis de resultados\n")
    print("-----------------------------------------------")
    print("      MENU ANALISIS DE RESULTADOS              ")
    print("-----------------------------------------------")
    print("[1] Calcular la media/promedio")    
    print("[2] Calcular la mediana")
    print("[3] Calcular la moda")
    print("[4] Calcular el valor máximo")
    print("[5] Calcular el valor mínimo")    
    print("[6] Comparar resultados entre experimentos")
    print("[7] Ir menú principal")
    opcion = input("Digite opción: ")
    try:
      opcion = int(opcion)      
    except:
      os.system("cls")
      print(f"La opción digitada '{opcion}' no es válida.\n")
    else:
      if (opcion < 1 or opcion > 7):          
        os.system("cls")
        print(f"La opción digitada '{opcion}' no es válida.\n")          
      else:            
        #Calcular media          
        if opcion == 1:                            
          calcularMedia(listaExperimentos)      
        elif opcion == 2:
          calcularMediana(listaExperimentos)
        elif opcion == 3:
          print("opción 3")
        elif opcion == 4:
          calcularMaximoMinimo(listaExperimentos,"maximo")
        elif opcion == 5:
          calcularMaximoMinimo(listaExperimentos,"minimo")
        elif opcion == 6:
          print("opción 6")
        #Ir al menú principal
        elif opcion == 7:
          menuPrincipal.menu(listaExperimentos)
          break
        
        
    print("\n[Esc] para volver al menú.") 
    key= None
    while key != b'\x1b':
      key = msvcrt.getch()

    os.system("cls")

#Función para solicitar al usuario entrada del ID de experimento y validar respuesta
def validarEntrada():
  #Solicita  el id del experimento  
  id = input("Digite el Id del experimento: ")
  #Valida la entrada realiza por el usuario
  if len(id) == 0:            
    print(f"El Id del experimento {id}, no es válido.")
    return -1
  return id

#Función para calcular la media o promedio
def calcularMedia(listaExperimentos):  
  os.system("cls")
  print("Menú de opciones / Análisis de resultados / Calcular media\n")
  #Llamar la función validarEntrada(), para solicitar y validar la entrada del ID, 
  #respuesta -1 entrada no valida, sale de la funcion, caso contrario continua su ejecución
  id= validarEntrada()   
  if id == -1:
    return False
  
  #LLamar la función para buscar experimento
  resultado= menuGestion.buscarExperimentos(listaExperimentos,id)
  #Si respuesta es -1, no se encontro ningun experimento con el ID
  if resultado == -1:
    print(f"Experimento Id {id}, no registrado en sistema.")
    return False
  else:
    #Llamar a la función mostrarInformacionExperimento del modulo menuGestion 
    menuGestion.mostrarInformacionExperimento(listaExperimentos[resultado])

    #Calcular el promedio de los resultados del experimento
    valores= listaExperimentos[resultado]['resultados']
    sumaValores = 0
    for valor in valores:
      sumaValores += valor
    
    media= round(sumaValores/len(valores),2)
    print(f"\nLa media/promedio, para el experimento es: {media}")

#Función para calcular la mediana  
def calcularMediana(listaExperimentos):  
  os.system("cls")
  print("Menú de opciones / Análisis de resultados / Calcular mediana\n")
  #Llamar la función validarEntrada(), para solicitar y validar la entrada del ID, 
  #respuesta -1 entrada no valida, sale de la funcion, caso contrario continua su ejecución
  id= validarEntrada()   
  if id == -1:
    return False
  
  #LLamar la función para buscar experimento
  resultado= menuGestion.buscarExperimentos(listaExperimentos,id)
  #Si respuesta es -1, no se encontro ningun experimento con el ID
  if resultado == -1:
    print(f"Experimento Id {id}, no registrado en sistema.")
    return False
  else:
    #Llamar a la función mostrarInformacionExperimento del modulo menuGestion 
    menuGestion.mostrarInformacionExperimento(listaExperimentos[resultado])

    #Calcular la mediana de los resultados del experimento
    valores= listaExperimentos[resultado]['resultados']
    #1. Ordenar los valores de menor a mayor
    valores.sort()
    #2. Encontrar la cantidad de datos
    cantidad= len(valores)
    #3. 
    #Si la cantidad de datos es impar, la mediana es el valor que se encuentra en el centro.    
    #Buscar el item de elemento del medio de la lista
    item= (cantidad // 2)
    if (cantidad % 2) != 0:
      mediana= round(valores[item],2)
    #Si el número de datos es par, la mediana es el promedio de los dos valores que están en el centro.
    else:
      promedio= (valores[item-1] + valores[item]) / 2
      mediana= round(promedio,2)
      
    print(f"\nLa mediana, para el experimento es: {mediana}")

#Función para calcular el valor maximo o mínimo  
def calcularMaximoMinimo(listaExperimentos,tipo):  
  os.system("cls")
  print(f"Menú de opciones / Análisis de resultados / Calcular valor {tipo}\n")
  #Llamar la función validarEntrada(), para solicitar y validar la entrada del ID, 
  #respuesta -1 entrada no valida, sale de la funcion, caso contrario continua su ejecución
  id= validarEntrada()   
  if id == -1:
    return False
  
  #LLamar la función para buscar experimento
  resultado= menuGestion.buscarExperimentos(listaExperimentos,id)
  #Si respuesta es -1, no se encontro ningun experimento con el ID
  if resultado == -1:
    print(f"Experimento Id {id}, no registrado en sistema.")
    return False
  else:
    #Llamar a la función mostrarInformacionExperimento del modulo menuGestion 
    menuGestion.mostrarInformacionExperimento(listaExperimentos[resultado])
    
    #Obtener la lista de valores del experimento
    valores= listaExperimentos[resultado]['resultados']
    if tipo.lower() == "maximo":    
      #Ordenar lista de mayor a menor
      valores.sort(reverse = True)
    else:
      #Ordenar lista de menor a mayor
      valores.sort()
    #Retornar el primer elimento de la lista     
    print(f"\nEl valor {tipo} del experimento es: {valores[0]}")


#mostrarMenu([{'id': 1, 'nombre': 'E1', 'fecha': "15/02/2025", 'tipo': 'Q', 'resultados': [2,3,5,3,7,8,3,9]}])