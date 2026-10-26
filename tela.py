import customtkinter as ctk  


class TelaVendas(ctk.CTkFrame):

  def __init__(self, parent):
    super().__init__(parent)

    #  Configura a grade principal da tela dividida em 2 colunas e 1 linha
    self.grid_columnconfigure(
        0, weight=1
    )  # Coluna 0 (Esquerda - Formulário)
    self.grid_columnconfigure(
        1, weight=2
    )  # Coluna 1 (Direita - Carrinho/Cupom - maior)
    self.grid_rowconfigure(0, weight=1)  # A altura ocupa toda a tela

    # Criação do Painel Esquerdo (Onde o operador digita os produtos)
    self.frame_left = ctk.CTkFrame(
        self
    )  # 'self' significa que ele fica dentro da TelaVendas
    self.frame_left.grid(
        row=0, column=0, sticky="nsew", padx=10, pady=10
    )  # Posicionado na coluna 0

    #Criação do Painel Direito (Onde aparece a lista do carrinho)
    self.frame_right = ctk.CTkFrame(self)
    self.frame_right.grid(
        row=0, column=1, sticky="nsew", padx=10, pady=10
    )  # Posicionado na coluna 1

    #função para criar os widgets do painel esquerdo
    self.criar_widgets_frame_left()
    #função para criar os widgets do painel direito
    self.criar_widgets_frame_right()

    def criar_widgets_frame_left(self):
        # Criação do título do painel esquerdo
        self.label_titulo = ctk.CTkLabel(
            self.frame_left, text="Vendas", font=("Arial", 20)
        )
        self.label_titulo.pack(pady=10)

        # Criação do campo de entrada para o código do produto
        self.entry_codigo_produto = ctk.CTkEntry(
            self.frame_left, placeholder_text="Código do Produto"
        )
        self.entry_codigo_produto.pack(pady=10)

        # Criação do botão para adicionar o produto ao carrinho
        self.botao_adicionar = ctk.CTkButton(
            self.frame_left, text="Adicionar ao Carrinho", command=self.adicionar_ao_carrinho
        )
        self.botao_adicionar.pack(pady=10)
        self.botao_adicionar.configure(width=200)  # Define a largura do botão
        self.botao_adicionar.configure(height=40)  # Define a altura do botão
        self.botao_adicionar.configure(font=("Arial", 12))  # Define a fonte do botão
        self.botao_adicionar.configure(fg_color="#4CAF50")  # Define a cor de fundo do botão
        self.botao_remover = ctk.CTkButton(
            self.frame_left, text="Remover do Carrinho", command=self.remover_do_carrinho
        )
        self.botao_remover.pack(pady=10)
        self.botao_remover.configure(width=200)  # Define a largura do botão
        self.botao_remover.configure(height=40)  # Define a altura do botão
        self.botao_remover.configure(font=("Arial", 12))  # Define a fonte do botão
        self.botao_remover.configure(fg_color="#F44336")  # Define a cor de fundo do botão  

    def criar_widgets_frame_right(self):
        # Criação do título do painel direito
        self.label_titulo_carrinho = ctk.CTkLabel(
            self.frame_right, text="Carrinho de Compras", font=("Arial", 20)
        )
        self.label_titulo_carrinho.pack(pady=10)

        # Criação da lista para exibir os produtos adicionados ao carrinho
        self.lista_carrinho = ctk.CTkTextbox(self.frame_right, width=300, height=400)
        self.lista_carrinho.pack(pady=10)

    def adicionar_ao_carrinho(self):
        codigo_produto = self.entry_codigo_produto.get()
        if codigo_produto:
            self.lista_carrinho.insert("end", f"{codigo_produto}\n")
            self.entry_codigo_produto.delete(0, "end")  # Limpa o campo de entrada
    def remover_do_carrinho(self):
        codigo_produto = self.entry_codigo_produto.get()
        if codigo_produto:
            conteudo = self.lista_carrinho.get("1.0", "end").strip().split("\n")
            if codigo_produto in conteudo:
                conteudo.remove(codigo_produto)
                self.lista_carrinho.delete("1.0", "end")
                self.lista_carrinho.insert("1.0", "\n".join(conteudo))
                self.entry_codigo_produto.delete(0, "end")  # Limpa o campo de entrada
    