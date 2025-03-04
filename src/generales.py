import os

#Función para limpiar la pantalla de la terminal
def limpiarPantalla():
  # Para sistemas Windows
  if os.name == 'nt':
      os.system('cls')
  # Para sistemas Unix (Linux/MacOS)
  else:
      os.system('clear')