from tkinter import*

windows = Tk()

#soamtorio função
def somatorio(n):
    s = 0
    for cont in range(1, n + 1):
        cont = cont + 1
        s = s + cont
        return (s)


#safadometro
def bt_click():
    if (str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()and str(ed3.get()).isnumeric() ):
        dia = int(ed1.get())
        mes = int(ed2.get())
        ano = int(ed3.get())
        safado = somatorio(mes) + (ano / 100) * (50 - dia)
        anjo = 100 - safado
        lb["text"] = "%.2f  porcento  anjo  " %anjo
        lb1["text"] ="Mais aquele %.2f porcento é vagabundo"%safado

    else:
        lb["text"] = "os valores informados são invalidos. "
        lb1["text"] = "os valores informados são invalidos. "

#entrada de dados
ed1 = Entry(windows)
ed1.place(x=100, y=100)

ed2 = Entry(windows)
ed2.place(x=100, y=150)

ed3 = Entry(windows)
ed3.place(x=100, y=200 )

#botão
btn = Button(windows, width= 15, text = "vai!", command= bt_click)
btn.place(x=100, y=250)

lb =Label(windows, text="", bg="green")
lb.place(x = 100 , y = 300)

lb1 =Label(windows, text="", bg="#FF1493")
lb1.place(x= 100 ,y= 350 )

windows.title ("Safadometro")
windows["bg"] = "black"
windows.geometry("300x400+150+150")
windows.mainloop()