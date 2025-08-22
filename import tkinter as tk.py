import tkinter as tk

# criar a janela principal 
root = tk.tk ()
root.title ("aplicativo hello word")
root.geometry ("300x100") # Definir tamanho da janela

#Adicionar um rotulo com a mensagem 
label = tk.label (root, text = "Olá, mundo!", font= "Arial", 16))
label.pack (pady= 20 ) #Adicionar espaçamento 

#iniciar loop principal da aplicação 

root.mainloop ()