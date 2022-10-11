import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()

root.title('Extrator de Texto')
root.resizable(False, False)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0, pady=20)


#Título
titulo = tk.Label(root, text="Selecione um arquivo PDF para extrair todo seu texto!", font="Rockwell")
titulo.grid(columnspan=3, column=0, row=1, pady=20)


def open_file():
    browse_text.set("Carregando...")
    file = askopenfile(parent=root, mode='rb', title='Selecione um arquivo', filetype=[("Arquivo pdf","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extract_text()
        
        #Caixa de texto
        text_box = tk.Text(root, height=15, width=75, padx=30, pady=30)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        
        #Reescrever botão
        browse_text.set("Selecionar")
     
#Botão Selecionar
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Rockwell", bg="#31d618", fg="white", height=2, width=15)
browse_text.set("Selecionar")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)


root.mainloop()
      


      






      





   
   
   
   
























