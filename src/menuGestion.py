from datetime import datetime
import menuPrincipal
import msvcrt
import generales

#Funcion para mostrar el submenú "GESTION DE EXPERIMENTOS"
def mostrarMenu(listaExperimentos):
  #Limpiar la pantalla
  generales.limpiarPantalla() 
  #Inicializar un ciclo para interactuar con el submenú  
  while True: 
    print("Menú de opciones / Gestión experimentos\n")
    print("-----------------------------------------------")
    print("      MENU GESTION DE EXPERIMENTOS             ")
    print("-----------------------------------------------")
    print("[1] Agregar nuevo experimento")    
    print("[2] Eliminar experimento")
    print("[3] Listar experimentos")
    print("[4] Ir menú principal")
    opcion = input("Digite opción: ")
    try:
      opcion = int(opcion)      
    except:
      generales.limpiarPantalla()
      print(f"La opción digitada '{opcion}' no es válida.\n")
    else:
      if (opcion < 1 or opcion > 4):          
        generales.limpiarPantalla()
        print(f"La opción digitada '{opcion}' no es válida.\n")          
      else:
        #Agregar experimento
        if opcion == 1:                            
          resultado= agregarExperimentos(listaExperimentos)                    
          if not resultado:
            print("\nNo se puede agregar el experimento")            
          else:
            print("\nExperimento agregado con éxito.")
        #Eliminar experimento
        elif opcion == 2:                            
          eliminarExperimentos(listaExperimentos)
        #Listar experimentos
        elif opcion == 3:                  
          listarTodosExperimentos(listaExperimentos)          
        #Ir al menú principal
        elif opcion == 4:
          menuPrincipal.menu(listaExperimentos)
          break
        
        
    print("\n[Esc] para volver al menú.") 
    key= None
    while key != b'\x1b':
      key = msvcrt.getch()

    generales.limpiarPantalla()
    
#Función para Agregar experimentos
def agregarExperimentos(listaExperimentos):  
  generales.limpiarPantalla()
  print("Menú de opciones / Gestión experimentos / Agregar experimento\n")
  
  #Solicita el nombre del experimento
  nombre = input("Digite el nombre del experimento: ")
  if not nombre:
    print("\nEl nombre del experimento es requerido por el sistema.")
    return False
  
  #Solicita la fecha del experimento
  fecha  = input("Digite la fecha de realización del experimento [DD/MM/AAAA]: ")
  #Validar la fecha digitada por el usuario en formato DD/MM/YY.    
  try:    
    fecha = datetime.strptime(fecha, '%d/%m/%Y')
  except:
      print(f"La fecha digitada {fecha}, no es válida.")
      return False
  
  #Solicita el tipo de experimento   
  tipo = input("Digite el tipo de experimento, [Q] Química - [F] Física - [B] Biología : ")
  #Valida que el tipo de experimento digitado sea correcto
  if tipo.upper() not in('Q','F','B') or not tipo:
    print(f"El tipo de experimento digitado {tipo} no es valido.")
    return False
  
  #Solicita lo resultados obtenidos del experimento
  entrada= input("Digite los resultados obtenidos, separados por coma. Recuerde que el sistema admite solo datos numericos.\nResultados: ")
  valores= entrada.split(",")
  resultados= []
  for valor in valores:
    try:
      resultados.append(float(valor))
    except ValueError:
      print(f"El valor ingresado {valor}, no es un dato numerico.")
      return False
    
  #Número consecutivo para identificar al experimento a grabar
  id= len(listaExperimentos)+1

  #Se realiza la creación de un diccionario para ingresar la información digitada por el usuario
  experimento = {"id": id, "nombre": nombre.upper(),"fecha":fecha,"tipo":tipo.upper(),"resultados":resultados}
  
  #Se agrega el diccionario a lista de experimentos
  listaExperimentos.append(experimento)
  return True
  
#Función para Listar todos los experimentos de la lista.
def listarTodosExperimentos(listaExperimentos):
  generales.limpiarPantalla()
  print("Menú de opciones / Gestión experimentos / Listar experimentos\n")

  i= 1
  #Inicializar un ciclo FOR para recorrer la lista experimentos
  for experimento in listaExperimentos:
    #Muestra en pantalla la información de los experimentos
    print("Experimento ",i)
    print("_____________________________________________")
    print("Id",' '*18,": ",experimento["id"])
    print("Nombre",' '*14,": ",experimento["nombre"])
    print("Fecha Realización",' '*3,": ",experimento["fecha"])
    if experimento["tipo"] == 'Q': tipo="QUIMICA"
    elif experimento["tipo"] == 'F': tipo="FISICA"
    elif experimento["tipo"] == 'B': tipo="BIOLOGIA"
    print("Tipo",' '*16,": ",tipo)
    print("Resultados Obtenidos  : ",experimento["resultados"])
    print("\n")
    i+=1

#Función para mostrar la información de un experimento en especifico
def mostrarInformacionExperimento(experimento):
  if len(experimento)>0:
    print(f"Id: {experimento['id']}")
    print(f"Nombre: {experimento['nombre']}")
    print(f"Fecha: {experimento['fecha']}")
    tipo= experimento['tipo']
    if tipo == 'Q': tipo="QUIMICA"
    elif tipo == 'F': tipo="FISICA"
    elif tipo == 'B': tipo="BIOLOGIA"
    print(f"Tipo: {tipo}")
    print(f"Resultados: {experimento['resultados']}")
  
#Función para buscar un experimento especifico.
def buscarExperimentos(listaExperimentos,id):
  #Inicializar un ciclo FOR para recorrer la lista de experimentos y buscar conforme al id
  i= 0
  for experimento in listaExperimentos:    
    if str(experimento["id"]) == str(id):      
      return i
    i+=1
  return -1
  
#Funcion para Eliminar un experimento de la lista.
def eliminarExperimentos(listaExperimentos):
  generales.limpiarPantalla()
  print("Menú de opciones / Gestión experimentos / Eliminar experimento\n")

  #Solicita  el id del experimento  
  id = input("Digite el Id del experimento: ")
  #Valida la entrada realiza por el usuario
  if len(id) == 0:
    print("Id no valido.")
    return False
  
  #LLamar la función para buscar experimento
  resultado= buscarExperimentos(listaExperimentos,id)
  #Si respuesta es -1, no se encontro ningun experimento con el ID
  if resultado == -1:
    print(f"Experimento Id {id}, no registrado en sistema.")
    return False
  else:
    nombre= listaExperimentos[resultado]['nombre']    
    mostrarInformacionExperimento(listaExperimentos[resultado])    
  
  #Inicializa un ciclo para solicitar al usuario confirmación de la eliminación
  while True:
    confirmar = input(f"\n¿Esta seguro que desea eliminar el Experimento Id {id}-{nombre}? S/N: ")
    if confirmar in ('S','s'):
      listaExperimentos.pop(resultado)
      print(f"\nExperimento Eliminado con éxito.")
      return True
    elif confirmar in('N','n'):
      print(f"\nOperación cancelada.")
      break
    print(f"Opción inválida.")
    
  return False