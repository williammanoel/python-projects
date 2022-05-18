from tkinter import *
root = Tk()
root.title('Calcular o troco ')
root.geometry("400x250")
root.resizable(False, False)
root.configure(background='#09A3BA')
def calcular():
    dr = dinheiro_recido.get()
    da = dinheiro_a_pagar.get()
    troco = dr-da
    if troco == 0:
        troco = 'Não existe troco, dinheiro recebido \né igual ao ' \
                'dinheiro a pagar.'
    elif troco <0:
        troco = 'Não existe troco, dinheiro recebido \né inferior' \
                ' ao dinheiro a pagar.'
    else:
        troco = troco
    return resultado.set(troco)
# Introduzir Valores

dinheiro_a_pagar_label = Label(text="Dinheiro a Pagar:",
                               background='#09A3BA',
              foreground="#FFFFFF")
dinheiro_a_pagar_label.place(relx=0.1,rely=0.1)
dinheiro_a_pagar = DoubleVar()
dpagar = Entry(textvariable=dinheiro_a_pagar)
dpagar.place(relx=0.4,rely=0.1)

dinheiro_recido_label = Label(text="Dinheiro Recebido:", background='#09A3BA',
              foreground="#FFFFFF")
dinheiro_recido_label.place(relx=0.1,rely=0.3)
dinheiro_recido = DoubleVar()
drecebido = Entry(textvariable=dinheiro_recido)
drecebido.place(relx=0.4,rely=0.3)

# Mostar Resultado
resultado = StringVar()
resultado_label = Label(text="Troco: ", background='#09A3BA',
              foreground="#FFFFFF")
resultado_label.place(relx=0.1,rely=0.7)
resultado1_label = Label(textvariable=resultado, background='#09A3BA',
                         foreground="#FFFFFF")
resultado1_label.place(relx=0.3,rely=0.7)

# Butão
result_button = Button(root, text="Calcular", command=calcular,
                       background='#09A3BA', foreground="#FFFFFF")
result_button.place(relx=0.4, rely=0.5)
mainloop()