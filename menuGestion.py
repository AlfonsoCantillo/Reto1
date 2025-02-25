from datetime import datetime
import os
import menuPrincipal
import msvcrt

#Funcion para mostrar el submenú "GESTION DE EXPERIMENTOS"
def mostrarMenu(listaExperimentos):
  #Limpiar la pantalla
  os.system("cls")
  #Inicializar un ciclo para interactuar con el submenú  
  while True: 
    print("-----------------------------------------------")
    print("      MENU GESTION DE EXPERIMENTOS             ")
    print("-----------------------------------------------")
    print("[1] Agregar nuevo experimento")
    print("[2] Actualizar experimento")
    print("[3] Eliminar experimento")
    print("[4] Listar experimentos")
    print("[5] Ir menú principal")
    try:
      opcion = int(input("Digite opción: "))      
    except:
      os.system("cls")
      print("La opción digitada es invalida_11\n")
    else:
      if (opcion < 1 or opcion > 5):          
        os.system("cls")
        print("La opción digitada es invalida_22\n")          
      else:
        if opcion == 1:                  
          agregarExperimentos(listaExperimentos)                    
        elif opcion == 3:                            
          eliminarExperimentos(listaExperimentos)
        elif opcion == 4:                  
          listarExperimentos(listaExperimentos)
          os.system("cls")
        elif opcion == 5:
          menuPrincipal.menu(listaExperimentos)
          break
    

#Función para Agregar experimentos
def agregarExperimentos(listaExperimentos):  
  os.system("cls")
  print("-----------------------------------------------")
  print("        AGREGAR NUEVO EXPERIMENTOS             ")
  print("-----------------------------------------------")
  #Solicita el nombre del experimento
  nombre = input("Digite el nombre del experimento: ")
  #Solicita la fecha del experimento
  fecha  = input("Digite la fecha de realización del experimento [DD/MM/AAAA]: ")
  #Validar la fecha digitada por el usuario en formato DD/MM/YY.    
  try:    
    fecha = datetime.strptime(fecha, '%d/%m/%Y')
  except:
      print("La fecha es inválida.")
  else: 
    #Solicita el tipo de experimento   
    tipo = input("Digite el tipo de experimento, [Q] Química - [F] Física - [B] Biología : ")
    #Valida que el tipo de experimento digitado sea correcto
    if tipo.upper() not in('Q','F','B'):
      print("El tipo de experimento digitado no es valido.")
    else:
      #Solicita lo resultados obtenidos del experimento
      print("Digite los resultados obtenidos. Recuerde que el sistema admite solo datos numericos.")
      print("[Esc] para salir / [Intro] para continuar.") 
      key = None 
      i= 1
      resultados = []
      #Se incializa un ciclo para que el sistema le solicite al usuario que ingrese los resultados
      #ESC para salir del ciclo
      while key != b'\x1b':  
        #Valida que el dato ingresado sea numerico        
        try:        
          r = float(input("Resultado " + str(i) +":  "))
          i+=1
          resultados.append(r)
          key = msvcrt.getch()
        except:
          print("Numero invalido.")

      #Validar que la información ingresada por el usuario este completa y correcta
      if not nombre or len(tipo) == 0 or len(resultados) == 0:
        print("Información incompleta, no se puede agregar el experimento.")
      else:
        id= len(listaExperimentos)+1
        #Se realiza la creación de un diccionario para ingresar la información digitada por el usuario
        experimento = {"id": id, "nombre": nombre.upper(),"fecha":fecha,"tipo":tipo.upper(),"resultados":resultados}
        #Se agrega el diccionario a lista de experimentos
        listaExperimentos.append(experimento)
        
        print("Experimento agregado a sistema.")

      print("\n[Esc] para salir") 
      key= None
      while key != b'\x1b':
        key = msvcrt.getch()

      os.system("cls")

  
#Funcion para Listar los experimentos, recibe la Lista de experimentos agregados a sistema
def listarExperimentos(listaExperimentos):
  os.system("cls")
  print("-----------------------------------------------")
  print("               LISTAR EXPERIMENTOS             ")
  print("-----------------------------------------------")
  i= 1
  #Inicializar un ciclo FOR para recorrer la lista experimentos
  for experimento in listaExperimentos:
    #Muestra en pantalla la información de los experimentos
    print("Experimento ",i)
    print("_____________________________________________")
    print("Id",' '*18,": ",experimento["id"])
    print("Nombre",' '*14,": ",experimento["nombre"])
    print("Fecha Realización",' '*3,": ",experimento["fecha"])
    print("Tipo",' '*16,": ",experimento["tipo"])
    print("Resultados Obtenidos  : ",experimento["resultados"])
    print("\n")
    i+=1

  print("[Esc] para salir") 
  key= None
  while key != b'\x1b':
    key = msvcrt.getch()

#Funcion para Eliminar un experimento de la lista, recibe la Lista de experimentos agregados a sistema
def eliminarExperimentos(listaExperimentos):
  os.system("cls")
  print("-----------------------------------------------")
  print("           ELIMINAR EXPERIMENTOS               ")
  print("-----------------------------------------------")
  #Solicita el id del experimento
  print(listaExperimentos[0])
  id = input("Digite el Id del experimento: ")
  if len(id) == 0:
    print("Id no valido")
  else:
    #Inicializar un ciclo FOR para recorrer la lista experimentos y buscar conforme al id 
    #digitado por el usuario
    i= 0
    for experimento in listaExperimentos:
      print(f"experimentoID {experimento["id"]}")
      print(f"ID {id}")
      if str(experimento["id"]) == str(id):
        listaExperimentos.pop(i)
        print(f"Experimento {experimento["id"]}-{experimento["nombre"]} Eliminado con éxito.")

      i+=1

    print("[Esc] para salir") 
    key= None
    while key != b'\x1b':
      key = msvcrt.getch()