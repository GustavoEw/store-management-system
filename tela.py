import tkintercustom as ctk
class TelaVendas(ctk.CTkFrame): 
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(1,weight=1)
        
        
