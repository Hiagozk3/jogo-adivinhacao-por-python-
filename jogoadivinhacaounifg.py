import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, master):
        self.master = master
        master.title("ADS FG - Jogo de Adivinhação")
        master.geometry("350x300")
        
        # Lógica do jogo

        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

        # --- Interface gráfica ---
        # 1. Título

        self.label_titulo = tk.Label(master, text="Adivinhe o Número\n(1 a 100)", font=("Arial", 16))
        self.label_titulo.pack(pady=20)

        # Campo de entrada (onde o usuario digita)
        
        self.entrada_chute = tk.Entry(master, font=("Arial", 12))
        self.entrada_chute.pack(pady=10)

        # Botão para Enviar o chute

        self.botao_chutar = tk.Button(
            master, text="Chutar!", command=self.processar_chute,
            bg="#4CAF50", fg="white", font=("Arial", 12)
        )
        self.botao_chutar.pack(pady=10)

        # Área de Feedback (Dicas)

        self.label_feedback = tk.Label(master, text="", font=("Arial", 10), fg="blue")
        self.label_feedback.pack(pady=10)

        # Botão para Reiniciar o jogo

        self.botao_reiniciar = tk.Button(
            master, text="Reiniciar Jogo", command=self.reiniciar, font=("Arial", 8)
        )
        self.botao_reiniciar.pack(side="bottom", padx=10)

    # Funções que unem a lógica do jogo com a interface gráfica

    def processar_chute(self):
        try:
            chute = int(self.entrada_chute.get()) # Pega o valor digitado
            self.tentativas += 1
            self.entrada_chute.delete(0, tk.END) # Limpa o campo de entrada

            if chute < 1 or chute > 100:
                self.label_feedback.config(text="Erro: Digite entre 1 e 100!", fg="red")

            elif chute == self.numero_secreto:
                messagebox.showinfo(
                    "Parabéns!",
                    f"Você acertou!\nNúmero: {self.numero_secreto}\nTentativas: {self.tentativas}"
                )
                self.label_feedback.config(text="Você ganhou!", fg="green")
                self.botao_chutar.config(state="disabled") # Desabilita o botão após ganhar

            elif chute > self.numero_secreto:
                self.label_feedback.config(text=f"Tentativa {self.tentativas}: É MENOR...", fg="blue")

            else:
                self.label_feedback.config(text=f"Tentativa {self.tentativas}: É MAIOR...", fg="blue")

        except ValueError:
            messagebox.showwarning("Entrada Inválida", "Por favor, digite apenas números válidos.")

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.entrada_chute.delete(0, tk.END)
        self.label_feedback.config(text="Jogo reiniciado!", fg="black")
        self.botao_chutar.config(state="normal") # Reabilita o botão
        
    # Inicialização do jogo

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
