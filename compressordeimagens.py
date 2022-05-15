 from tkinter import *
from tkinter.filedialog import *
from PIL import Image
from tkinter import messagebox


################# definir algumas cores ###############
co0 = "#000000"  # black
co1 = "#59656F"
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co5 = "#59b356"  # green

################## criar a janela principal do aplicativo ###############
janela = Tk()
# to prevent the window size from being changed
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('405x250')
janela.title('Compressor de imagem')
janela.configure(background=co2)


############ criando um frame ###########
framecima = Frame(janela, width=405, height=250, bg=co2, relief="flat",)
framecima.grid(row=0, column=0, sticky=NSEW)

######### adicionando um label que será exibido o nome do aplicativo #######
app_name = Label(framecima, text="Compressor de imagem", width=24, height=1, pady=7,
                 padx=10, relief="flat", anchor=CENTER, font=('Courier  20 bold'), bg=co2, fg=co0)
app_name.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=1)


# para abrir um novo arquivo
def novoArquivo():
    # Abre uma imagem
    ficheiro = askopenfilename()
    img = Image.open(ficheiro)

    # Tamanho da imagem em pixels (tamanho da imagem original)
    img_altura, img_largura = img.size
    tamanho_antigo = Label(framecima, text="Altura e Largura Original " + str(img_altura) + "x" + str(img_largura),
                           width=22, height=1, pady=7, padx=10, relief="flat", anchor=CENTER, font=('Courier  12 bold'), bg=co2, fg=co3)
    tamanho_antigo.grid(row=2, column=0, columnspan=2, sticky=NSEW, pady=5)

    # função para converter
    def converter():
        # obtendo os valores das entradas de altura e largura
        altura = int(entrada_altura.get())
        largura = int(entrada_largura.get())

        # Definindo novas dimensões para a imagem
        novo_tamanho = (altura, largura)
        nova_img = img.resize((novo_tamanho), Image.ANTIALIAS)
        img_salvar = asksaveasfilename()
        nova_img.save(img_salvar + ".JPG")
        messagebox.showinfo(
            'Sucesso', 'A imagem foi convertida com sucesso !!!')
        entrada_altura.destroy()
        entrada_largura.destroy()
        nova_altura.destroy()
        nova_largura.destroy()
        b_converter.destroy()
        tamanho_antigo.destroy()

    ############ Criando alguns Labes ##############
    nova_altura = Label(framecima, text="Digite nova altura", width=10, height=1, pady=7,
                        padx=10, relief="flat", anchor=CENTER, font=('Courier  9 bold'), bg=co2, fg=co0)
    nova_altura.grid(row=3, column=0,  sticky=NSEW, pady=5)
    nova_largura = Label(framecima, text="Digite nova largura", width=10, height=1, pady=7,
                         padx=10, relief="flat", anchor=CENTER, font=('Courier  9 bold'), bg=co2, fg=co0)
    nova_largura.grid(row=3, column=1,  sticky=NSEW, pady=5)

    entrada_altura = Entry(framecima, width=9, justify='center')
    entrada_altura.grid(row=4, column=0, sticky=NSEW, pady=5)
    entrada_largura = Entry(framecima, width=9, justify='center')
    entrada_largura.grid(row=4, column=1, sticky=NSEW, pady=5)

    ################# Botão Converter ##############
    b_converter = Button(framecima, text="Converter", width=10, height=1, bg=co5,
                         fg="white", font="5", anchor="center", relief=RAISED, command=converter)
    b_converter.grid(row=5, column=0, columnspan=2,  pady=5)


############# criar botão para o novo arquivo ##############
b_novo = Button(framecima, text="+ Novo", width=10, height=1, bg=co3,
                fg="white", font="5", anchor="center", relief=RAISED, command=novoArquivo)
b_novo.grid(row=1, column=0, columnspan=2, sticky=NSEW, pady=1)


janela.mainloop()