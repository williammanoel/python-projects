from tkinter import *
import random
root = Tk()
root.title("Lançar os dados")
root.geometry("500x400")
root.resizable(False, False)
label = Label(root, font=('helvetica', 250, 'bold'), text='')
def lancardados():
    dados = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684',
             '\u2685']
    label.configure(text=f'{random.choice(dados)}')
    label.place(relx=0.2, rely=0.15)
button = Button(root, font=('helvetica', 25, 'bold'),
                text='Lançar os dados',
                command=lancardados, bg="skyblue")
button.place(relx=0.2, rely=0.05)
root.mainloop()