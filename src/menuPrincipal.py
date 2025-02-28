import msvcrt
import os
import menuGestion
import menuAnalisis

#Función para mostrar en pantalla el menú principal del sistema
def menu(listaExperimentos):
  #Limpiar la pantalla
  os.system("cls")   
  #Inicializar un ciclo para interactuar con el menú  
  while True:
    print("Menú de opciones\n")  
    print("-----------------------------------------------")
    print("                  MENU DE OPCIONES             ")
    print("-----------------------------------------------")
    print("[1] Gestión de experimentos")
    print("[2] Análisis de resultados")
    print("[3] Generación de informes")
    print("[4] Salir del sistema")
    opcion = input("Digite opción: ")
    try:      
      opcion = int(opcion)  
    except ValueError:
      os.system("cls")
      print(f"La opción digitada '{opcion}' no es válida.")
    else:    
      #Validar la opción digitada por el usuario
      if (opcion not in(1,2,3,4)):          
        os.system("cls")
        print(f"La opción digitada '{opcion}' no es válida.\n")          
      else:        
        if opcion == 1:        
          menuGestion.mostrarMenu(listaExperimentos)
          break
        if opcion == 2:        
          menuAnalisis.mostrarMenu(listaExperimentos)
          break
        elif opcion == 4:
          os.system("cls") #Limpiar la pantalla
          print("Gracias por utilizar nuestros servicios.")  
          break

    print("\n[Esc] para volver al menú.") 
    key= None
    while key != b'\x1b':
      key = msvcrt.getch()

    os.system("cls")
          