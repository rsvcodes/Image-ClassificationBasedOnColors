# Image-ClassificationBasedOnColors
Proyecto de Clasificación de Imágenes por Color Predominante

Este proyecto tiene como objetivo desarrollar un sistema de clasificación de imágenes basado en el color predominante presente en cada imagen. Utilizamos un enfoque de clasificación no supervisada mediante el algoritmo de K-Means para agrupar los píxeles de las imágenes en clusters según la similitud de sus valores de color. Luego, clasificamos las imágenes en categorías como "girasol", "rosa" y "otros", dependiendo de los colores predominantes identificados en los clusters.

Instrucciones de Uso:

    Requisitos:
        Python 3.x
        Bibliotecas Python: OpenCV, NumPy, scikit-learn

    Instalación de Dependencias:
        Instala las bibliotecas necesarias ejecutando pip install -r requirements.txt en tu entorno virtual o sistema.

    Ejecución del Proyecto:
        Asegúrate de tener una carpeta con las imágenes que deseas clasificar.
        Ejecuta el script main.py, que cargará las imágenes, extraerá las características de color predominante y las clasificará en las categorías mencionadas.

    Resultados:
        El programa imprimirá el nombre de cada imagen junto con su clasificación según el color predominante identificado.
