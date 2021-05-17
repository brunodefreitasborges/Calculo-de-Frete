from tkinter import *


root = Tk()
root.title("Cálculo de Frete")
root.iconbitmap('icon.ico')
root.resizable(False, False)


# Functions

def calcular():
    cotacao = float(entry_cotacao.get())
    pedagio = float(entry_pedagio.get())
    frete = cotacao * float(entry_km.get())
    adiantamento = float(((frete / 100 * 75) + pedagio) - float(entry_abastecimento.get()))
    quitacao = float((frete / 100 * 25) + float(entry_entrega.get()))

    frete = '{:.2f}'.format(frete)
    adiantamento = '{:.2f}'.format(adiantamento)
    quitacao = '{:.2f}'.format(quitacao)

    entry_frete.delete(0, END)
    entry_ad.delete(0, END)
    entry_qt.delete(0, END)

    entry_frete.insert(0, frete)
    entry_frete.insert(0, "R$")
    entry_ad.insert(0, adiantamento)
    entry_ad.insert(0, "R$")
    entry_qt.insert(0, quitacao)
    entry_qt.insert(0, "R$")

    label_frete.grid(row=5, column=0, sticky="W")
    entry_frete.grid(row=5, column=1)
    label_ad.grid(row=6, column=0, sticky="W")
    entry_ad.grid(row=6, column=1)
    label_qt.grid(row=7, column=0, sticky="W")
    entry_qt.grid(row=7, column=1)
    
    if r.get() == 1:
        aliquota = (float(frete) / 100 * 20)
        inss = float((aliquota / 100 * 11))
        sestsenat = float((aliquota / 100 * 2.5))
        adiantamento = float(adiantamento) - (inss + sestsenat)
        inss = '{:.2f}'.format(inss)
        sestsenat = '{:.2f}'.format(sestsenat) 
        adiantamento = '{:.2f}'.format(adiantamento) 
        entry_ad.delete(0, END)
        entry_ad.insert(0, adiantamento)
        entry_ad.insert(0, "R$")
        entry_inss.delete(0, END)
        entry_sestsenat.delete(0, END)
        label_inss.grid(row=8, column=0, sticky="W")
        entry_inss.grid(row=8, column=1, sticky="E")
        entry_inss.insert(0, inss)
        entry_inss.insert(0, "R$")
        label_sestsenat.grid(row=9, column=0, sticky="W")
        entry_sestsenat.grid(row=9, column=1, sticky="E")
        entry_sestsenat.insert(0, sestsenat)
        entry_sestsenat.insert(0, "R$")
        
    
    if r.get() == 2:
        label_inss.grid_forget()
        entry_inss.grid_forget()
        label_sestsenat.grid_forget()
        entry_sestsenat.grid_forget()
        

def toggleEntrega():
    global showEntrega

    if showEntrega == True:
        entry_entrega.grid_forget()
        showEntrega = False
        
    elif showEntrega == False:
        entry_entrega.grid(row=2, column=1)
        showEntrega = True
      
        
    


def toggleAbastecimento():
    global showAbastecimento

    if showAbastecimento == True:
        entry_abastecimento.grid_forget()
        showAbastecimento = False
    
    elif showAbastecimento == False:
        entry_abastecimento.grid(row=3, column=1)
        showAbastecimento = True


r = IntVar()
showEntrega = bool(False)
showAbastecimento = bool(False)

# Definindo os Widgets
frame0 = LabelFrame(root, text="Pessoa", padx=24, pady=5)
frame1 = LabelFrame(root, text="Dados do Frete", padx=10, pady=10)
frame2 = LabelFrame(root, text="Valores do Frete", padx=20, pady=20)
radio_fisica = Radiobutton(frame0, text="Pessoa Física", variable=r, value=1)
radio_juridica = Radiobutton(frame0, text="Pessoa Jurídica", variable=r, value=2)
radio_juridica.select()
label_cotacao = Label(frame1, text="Cotação: R$")
entry_cotacao = Entry(frame1, width="5")
entry_cotacao.insert(END, 0)
label_pedagio = Label(frame1, text="  Pedágio: R$")
entry_pedagio = Entry(frame1, width="8")
entry_pedagio.insert(END, 0)
label_km = Label(frame1, text="Kilometragem:")
entry_km = Entry(frame1)
button_calcular = Button(root, text="Calcular", width=30, command=calcular)
entrega_check = Checkbutton(frame1, text="Entregas", command=toggleEntrega)
abastecimento_check = Checkbutton(frame1, text="Abastecimento", command=toggleAbastecimento)


# Hidden Widgets
label_frete = Label(frame2, text="Frete: ")
entry_frete = Entry(frame2)
label_ad = Label(frame2, text="Adiantamento: ")
entry_ad = Entry(frame2)
label_qt = Label(frame2, text="Quitação: ")
entry_qt = Entry(frame2)
entry_entrega = Entry(frame1)
entry_entrega.insert(END, 0)
entry_abastecimento = Entry(frame1)
entry_abastecimento.insert(END, 0)
label_inss = Label(frame2, text="INSS: ")
entry_inss = Entry(frame2)
entry_inss.insert(END,0)
label_sestsenat = Label(frame2, text="SEST/SENAT: ")
entry_sestsenat = Entry(frame2)
entry_sestsenat.insert(END, 0)


# Colocando na Tela
frame0.grid(row=0, column=0, padx=10, pady=10)
frame1.grid(row=1, column=0, padx=10, pady=10)
frame2.grid(row=3, column=0, padx=10, pady=10)
radio_fisica.grid(row=0, column=0)
radio_juridica.grid(row=0, column=1)
label_cotacao.grid(row=0, column=0, sticky="W")
entry_cotacao.grid(row=0, column=0, sticky="E")
label_pedagio.grid(row=0, column=1, sticky="W")
entry_pedagio.grid(row=0, column=1, sticky="E")
label_km.grid(row=1, column=0, sticky="W")
entry_km.grid(row=1, column=1)
entrega_check.grid(row=2, column=0, sticky="W")
abastecimento_check.grid(row=3, column=0, sticky="W")
button_calcular.grid(row=2, column=0, columnspan=2)

root.mainloop()
