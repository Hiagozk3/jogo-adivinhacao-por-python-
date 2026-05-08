import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, master): # Inicializa a classe do jogo, configurando a interface e a lógica do jogo
        self.master = master # Configurações da janela principal
        master.title("AdivinhaFG") # Título da Página
        master.state("zoomed")  # Abre maximizado no Windows
        master.configure(bg="#1e1e2e") # Cor de fundo da janela

        # Lógica do jogo
        self.numero_secreto = random.randint(1, 100) # Gera um número aleatório entre 1 e 100
        self.tentativas = 0 # Contador de tentativas do jogador
