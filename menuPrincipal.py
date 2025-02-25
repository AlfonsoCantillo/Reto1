import os
import menuGestion

#Función para mostrar en pantalla el menú principal del sistema
def menu(listaExperimentos):
  #Limpiar la pantalla
  os.system("cls") 
  #Inicializar un ciclo para interactuar con el menú  
  while True:  
    print("-----------------------------------------------")
    print("                  MENU DE OPCIONES             ")
    print("-----------------------------------------------")
    print("[1] Gestión de experimentos")
    print("[2] Análisis de resultados")
    print("[3] Generación de informes")
    print("[4] Salir del sistema")
    try:      
      opcion = int(input("Digite opción: "))  
    except:
      os.system("cls")
      print("La opción digitada es invalida_33")
    else:    
      #Validar la opción digitada por el usuario
      if (opcion not in(1,2,3,4)):          
        os.system("cls")
        print("La opción digitada es invalida_33\n")          
      else:
        print("La opción seleccionada es", opcion)
        if opcion == 1:        
          menuGestion.mostrarMenu(listaExperimentos)
          break
        elif opcion == 4:
          os.system("cls") #Limpiar la pantalla
          print("Gracias por utilizar nuestros servicios.")  
          break
          