import msvcrt
import menuPrincipal
import generales
import statistics
import os

#Funcion para generación de informes"
def generarInformes(listaExperimentos):
  #Limpiar la pantalla
  generales.limpiarPantalla() 
  print("Menú de opciones / Generación de informes\n")
  try:
    # Ruta del directorio donde guardar el archivo
    directorio = './reto1/data'
    # validar que existe el direcotio
    os.makedirs(directorio, exist_ok=True)
    # Ruta completa del archivo
    archivo = os.path.join(directorio, 'informe.txt')
    #Abrir el archivo para agregar la información
    f = open(archivo, "w", encoding='utf-8')
    f.write(f"INFORME GENERAL DE EXPERIMENTOS\n\n")
    #Inicializar un ciclo FOR para recorrer la lista experimentos
    for experimento in listaExperimentos:    
      f.write(f"Id experimento: {experimento["id"]}\n")
      f.write(f"Nombre experimento: {experimento["nombre"]}\n")
      f.write(f"Fecha Realización del experimento: {experimento["fecha"]}\n")
      if experimento["tipo"] == 'Q': tipo="QUIMICA"
      elif experimento["tipo"] == 'F': tipo="FISICA"
      elif experimento["tipo"] == 'B': tipo="BIOLOGIA"
      f.write(f"Tipo experimento: {tipo}\n")
      f.write(f"Resultados generales del experimento: {experimento["resultados"]}\n\n")

      promedio = round(statistics.mean(experimento["resultados"]),2)      
      mediana  = round(statistics.median(experimento["resultados"]),2)     
      moda     = round(statistics.mode(experimento["resultados"]),2)      
      minimo   = min(experimento["resultados"])
      maximo   = max(experimento["resultados"])
      f.write(f"Conclusión\n")            
      f.write(f"Tras analizar los datos recopilados, se puede concluir:\n\n")      
      f.write(f"- Se mantiene una media de {promedio}, lo que indica el valor promedio general de los resultados.\n")
      f.write(f"- En cuanto a la mediana, se encontró que es de {mediana}, lo que sugiere que la mitad de los valores se encuentran por debajo de este punto, reflejando una distribución centrada. \n")
      f.write(f"- La moda, por su parte, se situó en {moda}, lo que indica que este fue el valor más frecuente dentro de los datos. \n")
      f.write(f"- El valor mínimo observado fue {minimo}, mientras que el máximo alcanzó {maximo}, lo que nos proporciona un rango de variabilidad entre los datos.  \n\n")
      f.write(f"------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

      f.write(f"\n")
    #Cerrar el archivo
    f.close()

    print(f'\nInforme creado con éxito en: {archivo}')

    print(f"\n[Esc] para volver al menú.") 
    key= None
    while key != b'\x1b':
      key = msvcrt.getch()
    
    #Volver al menu principal
    menuPrincipal.menu(listaExperimentos)

  except Exception as e:
    print(f"Ocurrió un error: {e}")