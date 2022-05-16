from tkinter import *
import webbrowser
import datetime
import time
root= Tk()
class alarme():
    def __init__(self):
        self.root = root
        self.janela()
        self.defenir_hora()
        root.mainloop()
    def janela(self):
        self.root.title("Hora de alarme")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
    def defenir_hora(self):
        self.texto = Label(root, font=('arial', 18, 'bold'),
              text="Alarme")
        self.texto.place(relx=0.05, rely=0.05)
        self.hrs = StringVar()
        self.hrbtn = Entry(root, textvariable=self.hrs, width=5,
                           font=('arial', 20, 'bold'))
        self.hrbtn.place(relx=0.05, rely=0.25)
        self.texto1 = Label(root, font=('arial', 10, 'bold'),
              text="Hora")
        self.texto1.place(relx=0.05, rely=0.45)

        self.min = StringVar()
        self.mint = Entry(root, textvariable=self.min, width=5,
                          font=('arial', 20, 'bold'))
        self.mint.place(relx=0.3, rely=0.25)
        self.texto2 = Label(root, font=('arial', 10, 'bold'),
              text="Minutos")
        self.texto2.place(relx=0.3, rely=0.45)

        self.sec = StringVar()
        self.sect = Entry(root, textvariable=self.sec, width=5,
                          font=('arial', 20, 'bold'))
        self.sect.place(relx=0.55, rely=0.25)
        self.texto3 = Label(root, font=('arial', 10, 'bold'),
              text="Segundos")
        self.texto3.place(relx=0.55, rely=0.45)

        self.setbtn = Button(root, text="Activar Alarme", bg="DodgerBlue2",
                fg="white",command=self.setalarm, font=('arial', 16, 'bold'))
        self.setbtn.place(relx=0.3, rely=0.6)


    def setalarm(self):
        horas = self.hrs.get()
        minutos = self.min.get()
        segundos = self.sec.get()
        alarmtime = f"{horas}:{minutos}:{segundos}"
        print(alarmtime)
        if (alarmtime != "::"):
            while True:
                time.sleep(1)
                time_now = datetime.datetime.now().strftime("%H:%M:%S")
                print(time_now)
                if time_now == alarmtime:
                    webbrowser.open('https://www.youtube.com/watch?v=wiscdBvN_D0'
                                    , new=2)
                    break
alarme()