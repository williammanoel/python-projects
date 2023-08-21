from tkinter import *
from tkinter import ttk
import requests
root =Tk()
class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
class convertermoeda(RealTimeCurrencyConverter):
    def __init__(self):
        self.root = root
        self.janela()
        self.aplicacao()
        root.mainloop()

    def janela(self):
        self.root.title("Converter Moedas")
        self.root.geometry("445x300")
        self.root.resizable(False, False)
    def aplicacao(self):
        # Moeda Inical
        self.moeda_inicial = StringVar()
        self.option1 = ['USD', 'EUR', 'BRL', 'JPY',
                        'GBP', 'CAD','CNY']
        self.texto1 = Label(text=" Moeda Inicial ",
                            font=("Helvetica", '10'))
        self.texto1.place(relx=0.15, rely=0.05)
        self.cb1 =ttk.Combobox(values= self.option1, width=10,
                               textvariable=self.moeda_inicial)
        self.cb1.place(relx=0.15, rely=0.2)
        # Moeda Final
        self.moeda_final = StringVar()
        self.option2 = ['USD', 'EUR', 'BRL', 'JPY', 'GBP',
                        'CAD', 'CNY']
        self.texto2 = Label(text=" Moeda Final ", font=("Helvetica", '10'))
        self.texto2.place(relx=0.55, rely=0.05)
        self.cb2 = ttk.Combobox(values=self.option2, width=10,
                                textvariable=self.moeda_final)
        self.cb2.place(relx=0.55, rely=0.2)

        # Montante
        self.montante = DoubleVar()
        self.montante_lb = Label(text=" Montante ", font=("Helvetica", '10'))
        self.montante_lb.place(relx=0.15, rely=0.45)
        self.montante_entry = Entry(textvariable=self.montante)
        self.montante_entry.place(relx=0.45, rely=0.45)

        # Butão de calcular o Total do produto
        self.bt_calcular = Button(text="Calcular", bd=2,
                                  font=('verdana', '8', 'bold'), bg='gray18',
                                  fg='white',
                                  command=self.butao1)
        self.bt_calcular.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)

        # Resultado
        self.resultadocambio = StringVar()
        self.lb_resultadocambio = Label(text="Resultado da Conversão",
                                 font=("Helvetica", '10', 'italic'))
        self.lb_resultadocambio.place(relx=0.15, rely=0.75)
        self.resultadocambio_lb2 = Label(textvariable=self.resultadocambio,
                                         font=("Helvetica", '8'))
        self.resultadocambio_lb2.place(relx=0.5, rely=0.75)

    def butao1(self):
      moedainicial = self.moeda_inicial.get()
      moedafinal = self.moeda_final.get()
      montantec = self.montante.get()
      # Converter
      url = 'https://api.exchangerate-api.com/v4/latest/USD'
      converterteste = RealTimeCurrencyConverter(url)
      a = round(converterteste.convert(moedainicial, moedafinal, montantec), 2)
      return self.resultadocambio.set(a)

convertermoeda()