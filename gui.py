from tkinter import Tk, Label, Button, Frame, Scrollbar, Text, END
import webbrowser

def mostrar_programas_gui(programas):
    def gerar_html(lista_programas):
        html_content = "<html><body>"
        html_content += "<table border='1'><tr><th>Nome</th><th>Versão</th></tr>"
        for programa in lista_programas:
            html_content += f"<tr><td>{programa['nome']}</td><td>{programa['versao']}</td></tr>"
        html_content += "</table></body></html>"
        
        with open("lista_programas.html", "w") as file:
            file.write(html_content)
        
        webbrowser.open_new_tab('lista_programas.html')

    icone = 'icone.ico'

    root = Tk()
    root.title("WinProgramLister - by Cassio Nhiemetz")
    root.iconbitmap(icone)
    frame = Frame(root)
    frame.pack()

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text_widget = Text(frame, wrap="word", yscrollcommand=scrollbar.set, width=120, height=35, bg="#8d9091")
    text_widget.pack(fill="both", expand=True)

    scrollbar["command"] = text_widget.yview

    for programa in programas:
        text_widget.insert(END, f"{programa['nome']} - {programa['versao']}\n")

    button = Button(root, text="Gerar HTML", command=lambda: gerar_html(programas))
    button.pack(pady=10)
    root.geometry("1000x600")
    root.configure(bg="#302E2F")

    root.mainloop()
