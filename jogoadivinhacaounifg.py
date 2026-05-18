import tkinter as tk # Importa a biblioteca tkinter, responsável por criar a interface gráfic
from tkinter import messagebox # Importa o módulo messagebox para exibir caixas de diálogo
import random # Importa o módulo random para gerar números aleatórios
from PIL import Image, ImageDraw, ImageTk # Importa a biblioteca Pillow para manipulação de imagens, usada no tema espacial

class JogoAdivinhacao:
    def __init__(self, master): # Inicializa a classe do jogo, configurando a interface e a lógica do jogo
        self.master = master # Configurações da janela principal
        master.title("AdivinhaFG") # Título da Página
        master.state("zoomed")  # Abre maximizado no Windows
        master.configure(bg="#1e1e2e") # Cor de fundo da janela

        # Lógica do jogo
        self.numero_secreto = random.randint(1, 100) # Gera um número aleatório entre 1 e 100
        self.tentativas = 0 # Contador de tentativas do jogador
        self.canvas_estrelas = None # Variável para armazenar o canvas de estrelas do tema espacial, inicialmente vazia
        self.fundo_espacial = None # Variável para armazenar a imagem de fundo do tema espacial, inicialmente vaziakklk
