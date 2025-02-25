<h2><b>Python - Reto 1: Proyecto de Simulación de Recopilación de Datos Experimentales de un Laboratorio.</b></h2>

Este proyecto simula un sistema para recopilar datos experimentales en un laboratorio ficticio. El objetivo es crear un entorno que permita gestionar la información de los experimentos y los resultados obtenidos, incorporando funcionalidades para procesar los datos y obtener conclusiones.

<h3><b>Descripción</b></h3>
El proyecto está diseñado para simular el proceso de recopilación de datos en un laboratorio. Utilizando Python, este sistema puede recopilar datos experimentales, análisis de resultados y generación de un informe final.

<h3><b>Funcionalidades principales</b></h3>
<ul>
  <li>
    <b>Menú de opciones:</b> El sistema es interactivo, a través de un menú de opciones permite al usuario seleccionar entre diferentes opciones.
  </li>
  <li>
    <b>Recopilación de datos experimentales:</b> El sistema permite agregar, visualizar y gestionar datos experimentales realizados en un laboratorio.
  </li>
  <li>
    <b>Análisis de resultados experimentales:</b> El sistema permite realizar operaciones básicas con los datos recopilados, como calcular promedios, máximos y mínimos de los resultados obtenidos
  </li>
  <li>
    <b>Generación informe final:</b> El sistema permite la generación de un informe resumen de los experimentos, incluyendo la descripción de los mismos y un análisis de los datos recopilados.
  </li>
</ul>

<h3>Instalación y ejecución</h3>
<ol>
  <li>
    <b>Clona el repositorio:</b><br>
    <i>git clone https://github.com/AlfonsoCantillo/Reto1.git</i>
  </li>
  <li>
    <b>Navega a la carpeta raíz del proyecto:</b><br>
    <i>cd /d/python/reto1/src/</i>
  </li>
  <li>
    <b>Ejecuta el archivo principal:</b><br>
    <i>python index.py</i>
  </li>
</ol>

<img src="/img/menu.png">  

<h3>Estructura del proyecto</h3>
El proyecto tiene la siguiente estructura de directorios:
Reto1/
|
|--img/                     # Carpeta para almacenar las imágenes del proyecto
|
|--src/                     # Código fuente del proyecto
|  |----index.py            # Script principal que realiza el llamado al menú interactivo
|  |----menuPrincipal.py    # Script para mostrar el menú principal
|  |----menuGestión.py      # Script con funciones para la gestión (CRUD) de experimentos
|   
|--README.md                # Este archivo
|
|--.gitignore               # Archivos y carpetas a ignorar por Git

<h3>Dependencias</h3>
Este proyecto utiliza las siguientes bibliotecas de Python:
<ul>
  <li><b>os:</b> Este módulo proporciona una manera de interactuar con el sistema operativo. Utilizado para limpiar pantalla</li>
  <li><b>datetime:</b> Este módulo proporciona clases para manipular fechas y horas de manera sencilla y eficiente.</li>
  <li><b>msvcrt:</b> Este módulo (Microsoft C Runtime Library) es específico de sistemas Windows y proporciona funciones relacionadas con la consola, como la lectura de entradas de teclado.</li>
</ul>

<h3>Desarrolladores</h3>
<ul>
  <li>ALFONSO RAFAEL CANTILLO IBARRA</li>
  <li>ALVARO ENRIQUE DIAZ QUIROZ</li>
</ul>
