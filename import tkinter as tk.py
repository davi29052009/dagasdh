import tkinter as tk 

janela = tk.Tk()
janela.title("minha primeira janela")
janela.geometry ("400x300")
janela.update_idletasks()
largura = janela.winfo_width()
altura = janela.winfo_height()
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f"400x300+{x}+{y}")
")

label = tk.label (
janela,
text = "janela criada com sucesso!"
font = ("Arial", 14)
justify = "center"
)