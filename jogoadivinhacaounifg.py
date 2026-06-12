import tkinter as tk # Importa a biblioteca tkinter, responsável por criar a interface gráfic
from tkinter import messagebox # Importa o módulo messagebox para exibir caixas de diálogo
import random # Importa o módulo random para gerar números aleatórios
from PIL import Image, ImageDraw, ImageTk # Importa a biblioteca Pillow para manipulação de imagens, usada no tema espacial


# =============================================================================
#  CLASSE: TelaBoasVindas
#  Primeira tela exibida ao abrir o jogo.
#  Coleta o nome do jogador (opcional) e, ao clicar em iniciar,
#  destrói seus próprios widgets e carrega o JogoAdivinhacao.
# =============================================================================

class TelaBoasVindas:

    # =========================================================================
    #  CONSTRUTOR
    #  Chamado automaticamente quando TelaBoasVindas() é instanciada.
    #  Recebe a janela principal e a função que abre o jogo.
    # =========================================================================
    def __init__(self, master, callback_iniciar):

        # ---------------------------------------------------------------------
        #  REFERÊNCIAS IMPORTANTES
        # ---------------------------------------------------------------------
        self.master = master                     # janela principal do tkinter
        self.callback_iniciar = callback_iniciar # função chamada ao clicar em "Iniciar"
                                                 # (recebe a janela e o nome digitado)

        # ---------------------------------------------------------------------
        #  CONFIGURAÇÃO DA JANELA
        # ---------------------------------------------------------------------
        self.master.title("AdivinhaFG")   # texto na barra de título da janela
        self.master.state("zoomed")        # abre a janela já maximizada
        self.master.configure(bg="#1e1e2e") # cor de fundo (roxo escuro do tema Catppuccin)

        # ---------------------------------------------------------------------
        #  FRAME PRINCIPAL
        #  Container invisível que agrupa todo o conteúdo da tela.
        #  place(relx=0.5, rely=0.5, anchor="center") o centraliza
        #  exatamente no meio da janela, independente do tamanho dela.
        # ---------------------------------------------------------------------
        self.frame_principal = tk.Frame(
            self.master,
            bg="#1e1e2e"
        )

        self.frame_principal.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ---------------------------------------------------------------------
        #  CHAMADA DOS MÉTODOS DE CONSTRUÇÃO DA INTERFACE
        # ---------------------------------------------------------------------
        self.criar_linha_decorativa()
        self.criar_titulos()
        self.criar_formulario()
        self.criar_rodape()

    # =========================================================================
    #  MÉTODOS DE CRIAÇÃO DA INTERFACE
    # =========================================================================

    def criar_linha_decorativa(self):
        # Canvas permite desenhar formas geométricas diretamente.
        # Aqui cria três retângulos coloridos lado a lado formando
        # uma barra decorativa que combina com as cores dos botões do jogo:
        #   verde   - cor do botão "Chutar"
        #   azul    - cor do feedback
        #   amarelo - cor do botão "Dica"

        self.canvas_linha = tk.Canvas(
            self.frame_principal,
            width=420,
            height=4,
            bg="#1e1e2e",
            highlightthickness=0  # remove a borda padrão do Canvas
        )

        self.canvas_linha.pack(pady=(0, 30)) # 0px acima, 30px abaixo

        self.canvas_linha.create_rectangle(  0, 0, 140, 4, fill="#a6e3a1", outline="") # verde
        self.canvas_linha.create_rectangle(140, 0, 280, 4, fill="#89b4fa", outline="") # azul
        self.canvas_linha.create_rectangle(280, 0, 420, 4, fill="#f9e2af", outline="") # amarelo

    # -------------------------------------------------------------------------

    def criar_titulos(self):
        # Ícone decorativo usando emoji
        self.label_icone = tk.Label(
            self.frame_principal,
            text="🎯",
            font=("Consolas", 52),
            bg="#1e1e2e"
        )
        self.label_icone.pack(pady=(0, 10))

        # Título principal em destaque
        self.label_titulo = tk.Label(
            self.frame_principal,
            text="AdivinhaFG",
            font=("Consolas", 42, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"  # texto claro sobre fundo escuro
        )
        self.label_titulo.pack(pady=(0, 4))

        # Subtítulo com descrição do jogo
        self.label_subtitulo = tk.Label(
            self.frame_principal,
            text="Jogo de Adivinhação",
            font=("Consolas", 14),
            bg="#1e1e2e",
            fg="#6c6f85"  # cor apagada para criar hierarquia visual
        )
        self.label_subtitulo.pack(pady=(0, 40))

    # -------------------------------------------------------------------------

    def criar_formulario(self):
        # Frame do formulário com fundo ligeiramente mais escuro
        # para criar profundidade e destacar a área de entrada do nome
        self.frame_formulario = tk.Frame(
            self.frame_principal,
            bg="#181825",
            padx=40,  # espaçamento interno lateral
            pady=30   # espaçamento interno vertical
        )
        self.frame_formulario.pack(pady=(0, 20))

        # Pergunta acima do campo de texto
        self.label_nome = tk.Label(
            self.frame_formulario,
            text="Como podemos te chamar?",
            font=("Consolas", 12, "bold"),
            bg="#181825",
            fg="#6c6f85"
        )
        self.label_nome.pack(anchor="w", pady=(0, 6)) # anchor="w" alinha à esquerda (West)

        # Campo onde o jogador digita o nome
        self.entrada_nome = tk.Entry(
            self.frame_formulario,
            font=("Consolas", 16),
            width=26,
            justify="left",              # texto começa da esquerda
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",  # cor do cursor de digitação
            relief="flat",
            bd=0                         # remove a borda padrão do campo
        )
        self.entrada_nome.pack(ipady=10, pady=(0, 6)) # ipady aumenta a altura interna do campo

        # Pressionar Enter também inicia o jogo (sem precisar clicar no botão)
        self.entrada_nome.bind(
            "<Return>",
            lambda evento: self.iniciar_jogo()
        )

        self.entrada_nome.focus() # cursor automático no campo ao abrir a tela

        # Aviso de que o campo é opcional
        self.label_opcional = tk.Label(
            self.frame_formulario,
            text="opcional — pode deixar em branco",
            font=("Consolas", 9, "bold"),
            bg="#181825",
            fg="#45475a"  # cor bem discreta para não chamar atenção
        )
        self.label_opcional.pack(anchor="w", pady=(0, 20))

        # Botão que inicia o jogo
        self.botao_iniciar = tk.Button(
            self.frame_formulario,
            text="Iniciar Jogo  →",
            command=self.iniciar_jogo, # chama iniciar_jogo() ao clicar
            bg="#a6e3a1",
            fg="#1e1e2e",
            font=("Consolas", 14, "bold"),
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2", # cursor de mãozinha ao passar pelo botão
            width=24
        )
        self.botao_iniciar.pack()

    # -------------------------------------------------------------------------

    def criar_rodape(self):
        # Texto pequeno e discreto no rodapé com a instrução do jogo
        self.label_rodape = tk.Label(
            self.frame_principal,
            text="Adivinhe o número secreto entre 1 e 100",
            font=("Consolas", 10, "bold"),
            bg="#1e1e2e",
            fg="#45475a"
        )
        self.label_rodape.pack(pady=(10, 0))


# =========================================================================
    #  INICIAR JOGO
    #  Lê o nome digitado, destrói todos os widgets da tela de boas-vindas
    #  e chama a função que abre o JogoAdivinhacao.
    # =========================================================================

    def iniciar_jogo(self):

        nome = self.entrada_nome.get().strip() # lê o nome e remove espaços nas bordas

        for widget in self.master.winfo_children(): # percorre todos os widgets da janela
            widget.destroy()                        # e os destrói antes de abrir o jogo

        self.callback_iniciar(self.master, nome) # abre JogoAdivinhacao passando a janela e o nome
        

class JogoAdivinhacao:

    
    def __init__(self, master, nome_jogador=""):

        self.master = master
        self.nome_joador = nome_jogador
if nome_jogador else "Jogador"

        self.master.title("AdvinhaFG")
self.master.configure(bg="#1e1e2e")

        self.numero_secreto =
random.randint(1, 100)
        self.tentativas = 0
        self.canvas_estrelas = None
       self.fundo_especial = None 

       self.criar_menus()
       self.criar_barra_superior()
       self.criar_interface_principal()

def criar_menus(self):

           # Menu de acessibilidade
self.menu_config = tk.Menu(self.master, tearoff=0)
self.menu_config.add_command(label="Alto Contraste", command=self.modo_alto_contraste)
self.menu_config.add_command(label="Daltônico", command=self.modo_daltonico)
self.menu_config.add_command(label="Normal", command=self.modo_normal)

            # Menu de temas
           self.menu_temas = 
tk.Menu(self.master, tearoff=0)

self.menu_temas.add_command(label="Espacial", command=self.tema_espacial)

self.menu_temas.add_command(label="Normal", command=self.modo_normal)
        

        
        
# =========================================================================
    #  BARRA SUPERIOR
    #  fill="x" faz o frame ocupar toda a largura da janela.
    #  side="top" o fixa no topo.
    # =========================================================================

    def criar_barra_superior(self):

        self.frame_topo = tk.Frame(self.master, bg="#181825", pady=8)
        self.frame_topo.pack(fill="x", side="top")

        # Nome do projeto à esquerda da barra
        self.label_topo = tk.Label(
            self.frame_topo,
            text="AdivinhaFG  |  Jogo de Adivinhação",
            font=("Consolas", 11),
            bg="#181825",
            fg="#6c6f85"
        )
        self.label_topo.pack(side="left", padx=15)

        # Botão que abre o menu de acessibilidade (à direita)
        self.botao_config = tk.Button(
            self.frame_topo,
            text="Acessibilidade",
            command=self.abrir_menu_acessibilidade,
            bg="#313244",
            fg="#cdd6f4",
            font=("Consolas", 10),
            relief="flat",
            padx=10,
            pady=4,
            cursor="hand2"
        )
        self.botao_config.pack(side="right", padx=15)

        # Botão que abre o menu de temas (à direita, ao lado do anterior)
        self.botao_temas = tk.Button(
            self.frame_topo,
            text="Temas",
            command=self.abrir_menu_temas,
            bg="#313244",
            fg="#cdd6f4",
            font=("Consolas", 10),
            relief="flat",
            padx=10,
            pady=4,
            cursor="hand2"
        )
        self.botao_temas.pack(side="right", padx=15)
        
 # =========================================================================
    #  INTERFACE PRINCIPAL
    #  expand=True faz o frame_central crescer e centralizar na janela.
    # =========================================================================

    def criar_interface_principal(self):

        # Frame que contém todo o conteúdo do jogo
        self.frame_central = tk.Frame(self.master, bg="#1e1e2e")
        self.frame_central.pack(expand=True)

        # Saudação personalizada com o nome do jogador
        self.label_saudacao = tk.Label(
            self.frame_central,
            text=f"Bem-vindo, {self.nome_jogador}!",
            font=("Consolas", 16),
            bg="#1e1e2e",
            fg="#a6e3a1"  # verde
        )
        self.label_saudacao.pack(pady=(30, 0))

        # Título principal
        self.label_titulo = tk.Label(
            self.frame_central,
            text="Adivinhe o Número",
            font=("Consolas", 36, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        self.label_titulo.pack(pady=(8, 5))

        # Instrução para o jogador
        self.label_subtitulo = tk.Label(
            self.frame_central,
            text="Um número entre 1 e 100 foi escolhido. Qual é este número?",
            font=("Consolas", 13),
            bg="#1e1e2e",
            fg="#6c6f85"
        )
        self.label_subtitulo.pack(pady=(0, 40))

        # Campo onde o jogador digita o número a ser chutado
        self.entrada_chute = tk.Entry(
            self.frame_central,
            font=("Consolas", 22),
            width=10,
            justify="center",            # centraliza o texto dentro do campo
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",  # cor do cursor de digitação
            relief="flat",
            bd=0                         # remove a borda do campo
        )
        self.entrada_chute.pack(pady=10, ipady=12) # ipady aumenta a altura interna

        # Pressionar Enter envia o chute sem precisar clicar no botão
        self.entrada_chute.bind(
            "<Return>",
            lambda evento: self.processar_chute()
        )

        self.entrada_chute.focus() # cursor automático no campo ao abrir o jogo

        # Cria os três botões (Chutar, Dica, Reiniciar)
        self.criar_botoes()

# Área de feedback — exibe "muito alto", "muito baixo", dicas, vitória, etc.
        # Começa vazio e é atualizado a cada interação do jogador.
        self.label_feedback = tk.Label(
            self.frame_central,
            text="",
            font=("Consolas", 14),
            bg="#1e1e2e",
            fg="#89b4fa"  # azul claro
        )
        self.label_feedback.pack(pady=20)

        # Contador de tentativas — atualizado a cada chute enviado
        self.label_tentativas = tk.Label(
            self.frame_central,
            text="Tentativas: 0",
            font=("Consolas", 11),
            bg="#1e1e2e",
            fg="#6c6f85"  # cor discreta para não distrair
        )
        self.label_tentativas.pack(pady=5)

    # =========================================================================
    #  BOTÕES
    #  Criados dentro de um frame para ficarem lado a lado na mesma linha.
    # =========================================================================

    def criar_botoes(self):

        # Frame que agrupa os três botões horizontalmente
        self.frame_botoes = tk.Frame(self.frame_central, bg="#1e1e2e")
        self.frame_botoes.pack(pady=20)

        # Botão "Chutar" — verifica o número digitado contra o número secreto
        self.botao_chutar = tk.Button(
            self.frame_botoes,
            text="Chutar!",
            command=self.processar_chute,
            bg="#a6e3a1",  # verde claro
            fg="#1e1e2e",
            font=("Consolas", 14, "bold"),
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2"
        )
        self.botao_chutar.pack(side="left", padx=10) # side="left" coloca botões lado a lado

        # Botão "Dica" — revela em qual faixa de 20 o número secreto está
        self.botao_dica = tk.Button(
            self.frame_botoes,
            text="Dica",
            command=self.processar_dica,
            bg="#f9e2af",  # amarelo claro
            fg="#1e1e2e",
            font=("Consolas", 14, "bold"),
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2"
        )
        self.botao_dica.pack(side="left", padx=10)

        # Botão "Reiniciar" — zera o jogo e sorteia um novo número
        self.botao_reiniciar = tk.Button(
            self.frame_botoes,
            text="↺ Reiniciar",
            command=self.reiniciar,
            bg="#313244",  # cor neutra para não competir com os outros botões
            fg="#cdd6f4",
            font=("Consolas", 14),
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2"
        )
        self.botao_reiniciar.pack(side="left", padx=10)
        
    # =========================================================================
    #  LÓGICA PRINCIPAL DO JOGO
    # =========================================================================

    def processar_chute(self):
        # Lê o valor digitado, compara com o número secreto e exibe o feedback.

        try:
            chute = int(self.entrada_chute.get()) # converte o texto digitado para inteiro

            self.tentativas += 1                  # incrementa o contador de tentativas
            self.entrada_chute.delete(0, tk.END)  # limpa o campo após enviar o chute
            self.label_tentativas.config(text=f"Tentativas: {self.tentativas}") # atualiza o contador na tela

            # Número fora do intervalo permitido
            if chute < 1 or chute > 100:
                self.label_feedback.config(
                    text="Digite um número entre 1 e 100!",
                    fg="#f38ba8"  # vermelho
                )

            # Jogador acertou o número secreto
            elif chute == self.numero_secreto:
                messagebox.showinfo(
                    "Parabéns!",
                    f" {self.nome_jogador}, você acertou!\n"
                    f"Número: {self.numero_secreto}\n"
                    f"Tentativas: {self.tentativas}"
                )
                self.label_feedback.config(text="Você ganhou!", fg="#a6e3a1")
                self.botao_chutar.config(state="disabled") # bloqueia o botão após a vitória

            # Chute foi maior que o número secreto
            elif chute > self.numero_secreto:
                self.label_feedback.config(
                    text="Muito alto! Tente um número menor.",
                    fg="#89b4fa"
                )

            # Chute foi menor que o número secreto
            else:
                self.label_feedback.config(
                    text="Muito baixo! Tente um número maior.",
                    fg="#89b4fa"
                )

        except ValueError:
            # Captura o erro caso o jogador digite letras ou caracteres inválidos
            messagebox.showwarning("Entrada Inválida", "Digite apenas números válidos.")

    # =========================================================================
    #  REINICIAR JOGO
    #  Sorteia um novo número e reseta o estado sem fechar a janela.
    # =========================================================================



    def reiniciar(self):

        self.numero_secreto = random.randint(1, 100) # novo número secreto
        self.tentativas = 0                           # zera o contador
        self.entrada_chute.delete(0, tk.END)          # limpa o campo de entrada
        self.label_feedback.config(text="Jogo reiniciado! Boa sorte.", fg="#89b4fa")
        self.label_tentativas.config(text="Tentativas: 0")
        self.botao_chutar.config(state="normal") # reabilita o botão caso estivesse bloqueado pela vitória
        self.entrada_chute.focus()               # volta o foco para o campo de entrada

    # =========================================================================
    #  DICA
    #  Divide o intervalo 1–100 em 5 faixas de 20 números e
    #  informa em qual delas o número secreto está.
    # =========================================================================

    def processar_dica(self):

        if self.numero_secreto <= 20:
            faixa = "1 e 20"
        elif self.numero_secreto <= 40:
            faixa = "21 e 40"
        elif self.numero_secreto <= 60:
            faixa = "41 e 60"
        elif self.numero_secreto <= 80:
            faixa = "61 e 80"
        else:
            faixa = "81 e 100"

        self.label_feedback.config(
            text=f"O número está entre {faixa}",
            fg="#f9e2af"  # amarelo
        )
      
    #Menus

    
    def abrir_menu_acessibilidade(self):
        self.menu_config.post(
            self.botao_config.winfo_rootx(),
            self.botao_config.winfo_rooty() + self.botao_config.winfo_height()
        )

    def abrir_menu_temas(self):
        self.menu_temas.post(
            self.botao_temas.winfo_rootx(),
            self.botao_temas.winfo_rooty() + self.botao_temas.winfo_height()
        )

    #Funções dos Temas:

    def remover_canvas(self):
        # Remove o fundo de estrelas do tema espacial, se estiver ativo.
        if self.canvas_estrelas is not None:
            self.canvas_estrelas.destroy()
            self.canvas_estrelas = None  # reseta a referência para None
            self.fundo_espacial  = None  # libera a imagem da memória

    def criar_fundo_espacial(self):
        # Gera uma imagem 1920x1080 com 200 estrelinhas brancas usando Pillow.
        largura = 1920
        altura  = 1080

        imagem = Image.new("RGB", (largura, altura), "#00008B") # fundo azul escuro
        draw   = ImageDraw.Draw(imagem)                          # objeto de desenho

        for _ in range(200):
            x = random.randint(0, largura)
            y = random.randint(0, altura)
            draw.ellipse([x, y, x+2, y+2], fill="white") # círculo branco de 2px = estrela

        return ImageTk.PhotoImage(imagem) # converte para formato compatível com tkinter

# =========================================================================
    #  TEMAS E ACESSIBILIDADE
    #  Cada função reconfigura as cores de todos os widgets.
    #  remover_canvas() é sempre chamada primeiro para limpar o fundo espacial.
    # =========================================================================

    def modo_alto_contraste(self):
        # Fundo preto e elementos brancos para máxima legibilidade.
        self.remover_canvas()
        bg = "black"

        self.master.configure(bg=bg)
        self.frame_topo.configure(bg=bg)
        self.frame_central.configure(bg=bg)
        self.frame_botoes.configure(bg=bg)

        self.label_topo.configure(bg=bg, fg="white")
        self.label_saudacao.configure(bg=bg, fg="white")
        self.label_titulo.configure(bg=bg, fg="white")
        self.label_subtitulo.configure(bg=bg, fg="white")
        self.label_feedback.configure(bg=bg, fg="white")
        self.label_tentativas.configure(bg=bg, fg="white")

        self.botao_chutar.configure(bg="white", fg="black")
        self.botao_dica.configure(bg="white", fg="black")
        self.botao_reiniciar.configure(bg="white", fg="black")
        self.botao_config.configure(bg="white", fg="black")
        self.entrada_chute.configure(bg="white", fg="black")

    # -------------------------------------------------------------------------

    def modo_daltonico(self):
        # Azul e laranja — par de cores distinguível pela maioria dos daltônicos.
        self.remover_canvas()
        bg = "#1a1a2e"

        self.master.configure(bg=bg)
        self.frame_topo.configure(bg="#0f0f1a")
        self.frame_central.configure(bg=bg)
        self.frame_botoes.configure(bg=bg)

        self.label_topo.configure(bg="#0f0f1a", fg="orange")
        self.label_saudacao.configure(bg=bg, fg="orange")
        self.label_titulo.configure(bg=bg, fg="orange")
        self.label_subtitulo.configure(bg=bg, fg="orange")
        self.label_feedback.configure(bg=bg, fg="orange")
        self.label_tentativas.configure(bg=bg, fg="orange")

        self.botao_chutar.configure(bg="blue", fg="white")
        self.botao_dica.configure(bg="orange", fg="black")
        self.botao_reiniciar.configure(bg="blue", fg="white")
        self.botao_config.configure(bg="blue", fg="white")
        self.entrada_chute.configure(bg="white", fg="black")

    # -------------------------------------------------------------------------

    def modo_normal(self):
        # Restaura o tema padrão Catppuccin Mocha.
        self.remover_canvas()
        bg = "#1e1e2e"

        self.master.configure(bg=bg)
        self.frame_topo.configure(bg="#181825")
        self.frame_central.configure(bg=bg)
        self.frame_botoes.configure(bg=bg)

        self.label_topo.configure(bg="#181825", fg="#6c6f85")
        self.label_saudacao.configure(bg=bg, fg="#a6e3a1")
        self.label_titulo.configure(bg=bg, fg="#cdd6f4")
        self.label_subtitulo.configure(bg=bg, fg="#6c6f85")
        self.label_feedback.configure(bg=bg, fg="#89b4fa")
        self.label_tentativas.configure(bg=bg, fg="#6c6f85")

        self.botao_chutar.configure(bg="#a6e3a1", fg="#1e1e2e")
        self.botao_dica.configure(bg="#f9e2af", fg="#1e1e2e")
        self.botao_reiniciar.configure(bg="#313244", fg="#cdd6f4")
        self.botao_config.configure(bg="#313244", fg="#cdd6f4")
        self.entrada_chute.configure(bg="#313244", fg="#cdd6f4")

    # -------------------------------------------------------------------------

    def tema_espacial(self):
        # Fundo azul escuro com estrelinhas geradas pelo Pillow.
        self.remover_canvas()
        bg = "#00008B"

        self.master.configure(bg=bg)
        self.frame_topo.configure(bg="#000066")
        self.frame_central.configure(bg=bg)
        self.frame_botoes.configure(bg=bg)

        self.label_topo.configure(bg="#000066", fg="#00ffff")
        self.label_saudacao.configure(bg=bg, fg="#00ffff")
        self.label_titulo.configure(bg=bg, fg="#00ffff")
        self.label_subtitulo.configure(bg=bg, fg="#00ffff")
        self.label_feedback.configure(bg=bg, fg="#00ffff")
        self.label_tentativas.configure(bg=bg, fg="#00ffff")

        self.botao_chutar.configure(bg="#4CAF50", fg="white")
        self.botao_dica.configure(bg="#f9e2af", fg="#1e1e2e")
        self.botao_reiniciar.configure(bg="#313244", fg="white")
        self.botao_config.configure(bg="#000066", fg="#00ffff")
        self.botao_temas.configure(bg="#000066", fg="#00ffff")
        self.entrada_chute.configure(bg="white", fg="#00008B")

        # Gera a imagem de estrelas e aplica como fundo da janela
        self.fundo_espacial  = self.criar_fundo_espacial()
        self.canvas_estrelas = tk.Label(self.master, image=self.fundo_espacial)
        self.canvas_estrelas.place(x=0, y=0, relwidth=1, relheight=1) # cobre 100% da janela

        self.canvas_estrelas.lower()  # empurra o fundo para trás de todos os outros widgets
        self.frame_topo.lift()        # traz a barra superior para frente
        self.frame_central.lift()     # traz o conteúdo do jogo para frente


# =============================================================================
#  PONTO DE ENTRADA
#  A condição abaixo garante que o código só executa quando o arquivo
#  é rodado diretamente — não quando é importado por outro arquivo.
# =============================================================================

if __name__ == "__main__":

    root = tk.Tk()                        # cria a janela principal
    TelaBoasVindas(root, JogoAdivinhacao) # exibe a tela de boas-vindas
    root.mainloop()                       # mantém o programa rodando e aguarda interações
