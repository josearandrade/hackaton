# Importar as bibliotecas necessárias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem TIFF em formato RGB

def load_image_rgb(img_paths):
    images = []
    
    # Carregar e converter cada imagem em RGB
    for img_path in img_paths:
        image = cv2.imread(img_path)
        if image is not None:  # Verifica se a imagem foi carregada corretamente
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            images.append(image_rgb)  # Adiciona a imagem convertida à lista
        else:
            print(f"Erro ao carregar a imagem: {img_path}")

    return images  # Retorna a lista de imagens



def processing_img(image):
    # Converter a imagem para escala de cinza   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    dilation = cv2.dilate(gray, kernel, iterations=1)

    closing = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)

    processed_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return processed_image



