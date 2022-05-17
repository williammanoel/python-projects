from tkinter import *

root = Tk()
root.title("Converter Temperatura")
root.geometry("300x150")
root.resizable(False,False)

def fahrenheit_para_celsius():
    fahrenheit = ent_temperaturaf.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
# Fahrenheit para CELSIUS
lab_temperaturaf = Label(root,text="Fahrenheit", font=("Arial","10","bold"))
lab_temperaturaf.place(relx=0.05,rely=0.05)
lab_temperaturaf = Label(root,text="Celsius", font=("Arial","10","bold"))
lab_temperaturaf.place(relx=0.45,rely=0.05)
ent_temperaturaf=DoubleVar()
ent_temperaturaf = Entry(textvariable=ent_temperaturaf)
ent_temperaturaf.place(relx=0.05,rely=0.2,relwidth=0.25)
btn_convert =Button(text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_para_celsius)
btn_convert.place(relx=0.35,rely=0.18)
lbl_result = Label(text="\N{DEGREE CELSIUS}")
lbl_result.place(relx=0.45,rely=0.18)

def celsius_para_fahrenheit():
    celsius = ent_temperaturac.get()
    fahrenheit = (9*float(celsius)+32*5)/5
    lbl_resultf["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"
# CELSIUS para Fahrenheit
lab_temperaturac = Label(root,text="Celsius", font=("Arial","10","bold"))
lab_temperaturac.place(relx=0.05,rely=0.35)
ent_temperaturac=DoubleVar()
ent_temperaturac = Entry(textvariable=ent_temperaturac)
ent_temperaturac.place(relx=0.05,rely=0.55,relwidth=0.25)
btn_convertf =Button(text="\N{RIGHTWARDS BLACK ARROW}",
    command= celsius_para_fahrenheit)
btn_convertf.place(relx=0.35,rely=0.55)
lbl_resultf = Label(text="\N{DEGREE FAHRENHEIT}")
lbl_resultf.place(relx=0.45,rely=0.55)
root.mainloop()