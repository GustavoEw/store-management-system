import customtkinter as ctk  # CORRIGIDO: O nome correto da biblioteca é customtkinter


class TelaVendas(ctk.CTkFrame):

  def __init__(self, parent):
    super().__init__(parent)

    # 1. Configura a grade principal da tela dividida em 2 colunas e 1 linha
    self.grid_columnconfigure(
        0, weight=1
    )  # Coluna 0 (Esquerda - Formulário)
    self.grid_columnconfigure(
        1, weight=2
    )  # Coluna 1 (Direita - Carrinho/Cupom - maior)
    self.grid_rowconfigure(0, weight=1)  # A altura ocupa toda a tela

    # 2. Criação do Painel Esquerdo (Onde o operador digita os produtos)
    self.frame_left = ctk.CTkFrame(
        self
    )  # 'self' significa que ele fica dentro da TelaVendas
    self.frame_left.grid(
        row=0, column=0, sticky="nsew", padx=10, pady=10
    )  # Posicionado na coluna 0

    # 3. Criação do Painel Direito (Onde aparece a lista do carrinho)
    self.frame_right = ctk.CTkFrame(self)
    self.frame_right.grid(
        row=0, column=1, sticky="nsew", padx=10, pady=10
    )  # Posicionado na coluna 1

    # 4. Título demonstrativo dentro do painel esquerdo
    ctk.CTkLabel(
        self.frame_left,
        text="🛒 Tela de Vendas",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(pady=20, padx=20)