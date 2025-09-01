import tkinter as tk 

janela = tk.Tk()
janela.title("janela colorida")
janela.geometry ("350x180")
janela.configure(bg="yellow")


def atividade_interatividade():
    # Layout da janela
    layout = [
        [sg.Text("Clique no botão", key='-ROTULO-', font=('Arial', 14))],
        [sg.Button("Clique Aqui", size=(15, 2), button_color=('white', 'blue'))],
        [sg.Button("Sair", button_color=('white', 'red'))]
    ]
    
    # Criar a janela
    window = sg.Window(
        "Interatividade", 
        layout, 
        element_justification='center',
        size=(300, 150)
    )
    
    # Loop de eventos
    while True:
        event, values = window.read()
        
        # Fechar a janela
        if event in (sg.WIN_CLOSED, "Sair"):
            break
        
        # Quando o botão é clicado
        if event == "Clique Aqui":
            window['-ROTULO-'].update("Botão clicado! ✅")
            window['Clique Aqui'].update(button_color=('white', 'green'))
    
    window.close()

# Executar o programa
if __name__ == "__main__":
    atividade_interatividade()

janela.mainloop()