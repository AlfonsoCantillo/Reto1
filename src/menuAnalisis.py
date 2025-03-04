import msvcrt
import menuGestion
import menuPrincipal
import generales
import statistics

#Funcion para mostrar el submenú "Análisis de resultados"
def mostrarMenu(listaExperimentos):
  #Limpiar la pantalla
  generales.limpiarPantalla() 
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
      generales.limpiarPantalla()
      print(f"La opción digitada '{opcion}' no es válida.\n")
    else:
      if (opcion < 1 or opcion > 7):          
        generales.limpiarPantalla()
        print(f"La opción digitada '{opcion}' no es válida.\n")          
      else:            
        #Calcular media          
        if opcion == 1:                            
          calcularMedia(listaExperimentos)      
        elif opcion == 2:
          calcularMediana(listaExperimentos)
        elif opcion == 3:
          calcularModa(listaExperimentos)
        elif opcion == 4:
          calcularMaximoMinimo(listaExperimentos,"maximo")
        elif opcion == 5:
          calcularMaximoMinimo(listaExperimentos,"minimo")
        elif opcion == 6:
          compararExperimentos(listaExperimentos)
        #Ir al menú principal
        elif opcion == 7:
          menuPrincipal.menu(listaExperimentos)
          break
        
        
    print("\n[Esc] para volver al menú.") 
    key= None
    while key != b'\x1b':
      key = msvcrt.getch()

    generales.limpiarPantalla()

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
  generales.limpiarPantalla()
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
  generales.limpiarPantalla()
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
    valores= listaExperimentos[resultado]['resultados'].copy()
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
  generales.limpiarPantalla()
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
    
    valores= listaExperimentos[resultado]['resultados']
    if tipo.lower() == "maximo":                      
      respuesta= max(valores)
    else:
      respuesta= min(valores)

    print(f"\nEl valor {tipo} del experimento es: {respuesta}")

#Función para calcular la moda
def calcularModa(listaExperimentos):
  generales.limpiarPantalla()
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

    #clonar la lista original
    valores= listaExperimentos[resultado]['resultados'].copy()
    #Diccionario temporal, para almacenar la cantidad de elementos repetidos
    temporal= {"elemento": 0, "cantidad":0}
    #Recorrer la lista y validar la cantidad de elementos repetidos  
    for x in valores:
      i= 0
      for j in valores:
        if x == j:
          i+=1

      if i > 1:
        if temporal["cantidad"] < i:
          temporal= {"elemento": [x], "cantidad":i}
        if temporal["cantidad"] == i and temporal["elemento"].count(x) == 0:
          elementos= temporal["elemento"]
          elementos.append(x)
          temporal= {"elemento": elementos, "cantidad":i}

    if temporal["cantidad"] == 0:
      print(f"\nLos resultados obtenidos del experimento, no tienen una moda")
    else:
      print(f"\nLa moda, para el experimento es: {temporal["elemento"]}")

#Función para comparar experimentos
def compararExperimentos(listaExperimentos):
  generales.limpiarPantalla()
  print("Menú de opciones / Análisis de resultados / Comparar resultados entre experimentos\n")
  
  #Solicita el id de los experimento a comparar
  ids = input("Digite el Id de los experimentos a comparar, separado por comas: ")
  ids = ids.split(",")
  #Valida la entrada realiza por el usuario
  if len(ids) <= 1:            
    print(f"Los Id(s) digitados {ids}, no son válidos.")
    return False

  for id in ids:  
    #LLamar la función para buscar experimento
    resultado= menuGestion.buscarExperimentos(listaExperimentos,id)
    #Si respuesta es -1, no se encontro ningun experimento con el ID
    if resultado == -1:
      print(f"Experimento Id {id}, no registrado en sistema.")
      #return False
    else:
      #Llamar a la función mostrarInformacionExperimento del modulo menuGestion 
      print("\n")
      menuGestion.mostrarInformacionExperimento(listaExperimentos[resultado])
      promedio = round(statistics.mean(listaExperimentos[resultado]["resultados"]),2)
      print(f"Promedio de resultado: {promedio}")
      
      