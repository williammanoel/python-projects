from tkinter import *
root =Tk()
class App():

    def __init__(self):
        self.root = root
        self.config()
        self.create_widgets()
        root.mainloop()

    def config(self):
        self.root.title("Tabuada")
        self.root.geometry("250x250")
        self.root.resizable(False, False)

    def create_widgets(self):
        self.result_label = Label(text="Digite um número: ")
        self.result_label.place(relx=0.35, rely=0.05)
        self.number = IntVar()
        self.number_entry = Entry(textvariable=self.number)
        self.number_entry.place(relx=0.35, rely=0.15)
        self.button =Button(text="ok", width=4, command=self.update_result)
        self.button.place(relx=0.4, rely=0.25, relwidth=0.25)


    def update_result(self):
        self.result_label["text"] = '\n'.join([
            "{x} * {y} = {result}".format(x=int(self.number_entry.get()),
                                        y=n,
                                          result=int(self.number.get()) * n)
                                        for n in range(1,11)])
        self.result_label.place(relx=0.42, rely=0.35)

App()