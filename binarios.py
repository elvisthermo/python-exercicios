from tkinter import*

janela = Tk()

def somatorio(n):
    s = 0
    for cont in range(1, n + 1):
        cont = cont + 1
        s = s + cont
        return (s)

def bt_click():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric() and str(ed3.get()).isnumeric()):
        ed1 = int(ed1.get())
        ed2 = int(ed2.get())
        ed3 = int(ed3.get())

    else:
        lb["text"] = "Os valores informados são invalidos! "


ed1 = Entry(janela)
ed1.place(x=100, y=100)

ed2 = Entry(janela)
ed2.place(x=100, y=150)

ed3 = Entry(janela)
ed3.place(x=100, y=200)


bt = Button(janela, width=15 ,text="calcular", command=bt_click)
bt.place(x=100, y=250)

lb = Label(janela, text="resultado")
lb.place(x=100, y=300)

janela.geometry("400x300+200+200")
janela.mainloop()