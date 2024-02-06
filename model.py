import os  # Importa el módulo para interactuar con el sistema operativo
import cv2  # Importa la biblioteca OpenCV para procesamiento de imágenes
import numpy as np  # Importa NumPy para operaciones numéricas
from sklearn.cluster import KMeans  # Importa KMeans de scikit-learn para agrupamiento

# Función para cargar las imágenes desde una carpeta
def cargar_imagenes(ruta, max_images=100):
    imagenes = []  # Lista para almacenar las imágenes
    total = min(max_images, len(os.listdir(ruta)))  # Calcula el límite de imágenes a cargar
    # Itera sobre los archivos en la carpeta
    for i, archivo in enumerate(os.listdir(ruta)):
        # Verifica si el archivo es una imagen JPEG y si se han cargado menos de max_images
        if archivo.endswith(".jpg") and i < max_images:
            # Lee la imagen, la redimensiona a 50x50 píxeles y la agrega a la lista
            imagen = cv2.imread(os.path.join(ruta, archivo))
            imagen = cv2.resize(imagen, (50, 50))
            imagenes.append(imagen)
            # Imprime información sobre la imagen cargada (nombre y tamaño)
            print(f"Cargando imagen {i+1}/{total}: {archivo}")
            print(f"Tamaño de la imagen {i+1}: {imagen.shape}")
    print("\n")  # Imprime una línea en blanco al final
    return imagenes  # Devuelve la lista de imágenes cargadas

# Función para extraer las características de color predominante de una imagen
def extraer_caracteristicas(imagen, k=3):
    # Convierte la imagen de BGR a RGB y la aplanada a una matriz 1D de píxeles
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    pixel_values = imagen.reshape((-1, 3))
    
    # Aplica el algoritmo de KMeans para agrupar los píxeles en k grupos
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixel_values)
    
    labels = kmeans.labels_  # Obtiene las etiquetas de los grupos
    centroids = kmeans.cluster_centers_  # Obtiene los centroides de los grupos
    
    # Calcula el índice del color predominante en la imagen
    color_predominante = np.argmax(np.bincount(labels))
    return color_predominante  # Devuelve el índice del color predominante

# Función para clasificar el color predominante en una categoría
def clasificar_color(color):
    if color == 0:
        return "Otros"
    elif color == 1:
        return "Girasol"
    elif color == 2:
        return "Rosa"
    else:
        return "Desconocido"

if __name__ == "__main__":
    # Ruta donde se encuentran las imágenes
    ruta_imagenes = r"C:\Users\agust\Desktop\proyecto_ia\images"
    
    # Carga las primeras 100 imágenes desde la ruta especificada
    imagenes = cargar_imagenes(ruta_imagenes, max_images=100)
    
    # Imprime el total de imágenes cargadas
    print(f"Total de imágenes cargadas: {len(imagenes)}")
    
    # Extrae características de color predominante de cada imagen
    features = [extraer_caracteristicas(imagen, k=3) for imagen in imagenes]
    
    # Imprime el total de características extraídas
    print(f"Total de características extraídas: {len(features)}")
    
    # Imprime la clasificación de cada imagen (color predominante)
    for i, color in enumerate(features):
        nombre_imagen = os.listdir(ruta_imagenes)[i]  # Obtiene el nombre de la imagen
        clasificacion = clasificar_color(color)  # Clasifica el color predominante
        print(f"Nombre de la imagen: {nombre_imagen} - Clasificación: {clasificacion}")  # Imprime la clasificación
