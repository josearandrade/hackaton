# This Python file uses the following encoding: utf-8
import sys

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.processing import *
from logic.utils import *
import config.settings as sett
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QListWidgetItem
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Grupy1
import json



class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Grupy1()
        self.ui.setupUi(self)


        # Conectar o botão ao método para selecionar imagens
        self.ui.importButton.clicked.connect(self.select_images)

        # Variável para armazenar os caminhos das imagens selecionadas
        self.image_paths = []
        self.file_names = []

        # Conectar o botão ao método para carregar as imagens
        self.ui.loadButton.clicked.connect(self.load_images)

        # Inicialmente, esconder a QLabel
        self.ui.load_OK.hide()  # Esconder a QLabel até que o carregamento seja concluído
        self.ui.load_OK_2.hide()
        
        # Conectar o botão ao método para carregar as imagens
        self.ui.processButton.clicked.connect(self.full_processing)

        # Conectar o botão ao método para exportar a lista
        self.ui.exportButton.clicked.connect(self.export_to_json)


    def select_images(self):
        # Abre o QFileDialog para selecionar imagens
        files, _ = QFileDialog.getOpenFileNames(self, "Select images", "", "Images (*.png *.jpg *.jpeg *.bmp *.tif)")

        if files:
            # Salva os caminhos das imagens selecionadas e os nomes dos arquivos
            self.image_paths = files
            self.file_names = [os.path.basename(file) for file in files]  # Lista com os nomes dos arquivos

            # Limpa a lista anterior e adiciona os novos nomes ao QListWidget
            self.ui.list_selected_images.clear()
            for file_name in self.file_names:
                QListWidgetItem(file_name, self.ui.list_selected_images)

    def load_images(self):
        # Verifica se há imagens selecionadas
        if self.image_paths:
            self.images = load_image_rgb(self.image_paths)  # Carrega as imagens e retorna a lista de imagens
            if self.images:  # Verifica se alguma imagem foi carregada
                self.ui.load_OK.setText("Load OK")  # Atualiza o texto da QLabel
                self.ui.load_OK.show()  # Mostra a QLabel
            else:
                self.ui.load_OK.setText("Erro ao carregar as imagens")
                self.ui.load_OK.show()  # Mostra a QLabel

    def full_processing(self):
        self.results = []  
        total_images = len(self.images)
        for idx, image in enumerate(self.images):  # Usa 'enumerate' para obter o índice da imagem
            image_name = self.file_names[idx]  # Pega o nome correto usando o índice
            
            # Atualiza a barra de progresso
            progress = int((idx + 1) / total_images * 100)
            self.ui.progressBar.setValue(progress)

            results = processing_img(image)

            result = "Serra Circular"
            if result == "Serra Circular":
                code = "MAT001"
            elif result == "Cabo Elétrico":
                code = "MAT801"
            elif result == "Chave de Fenda":
                code = "MAT901"
            elif result == "Alicate de Corte":
                code = "MAT902"
            elif result == "Chave Estrela":
                code = "MAT906"
            elif result == "Carrinho de Transporte de Bobinas": 
                code = "EQP502"

            # Formatação do texto do resultado para exibir no QListWidget
            self.result_text = f"Image: {image_name} | Code: {code} "

            # Criação e adição do item de resultado à lista
            item = QListWidgetItem(self.result_text)
            self.ui.codes_list.addItem(item)

    # Função para exportar os resultados para um arquivo JSON
    def export_to_json(self, filename=None):
        # Define um valor padrão caso `filename` não seja fornecido ou seja inválido
        filename = filename if isinstance(filename, str) else "results.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.result_text, f, ensure_ascii=False, indent=4)
            print(f"Resultados exportados para {filename} com sucesso.")
        except OSError as e:
            print(f"Erro ao exportar para {filename}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
