from tkinter import *
import Banco
import main


def PegarDados(name, valor):
    if name.get() != "" and valor.get() != "":
        vname = name.get()
        vquery = "SELECT * FROM tb_students WHERE T_NAME = ?"

        res = Banco.dql(vquery, (vname,))
        print(res)

    else:
        main.MsgBox('Algum Campo está em Branco')


def Limpar(name,valor):
    name.delete(0, END)
    valor.delete(0, END)



class Toplavelpayment(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('PAGAMENTO')
        self.geometry("400x300")


        self.lb_name = Label(self, text='Nome do Aluno', anchor=W,).place(x=10, y=20)
        self.tb_name = Entry(self)
        self.tb_name.place(x=10, y=40)

        self.titulo_valor = Label(self, text ='valor', anchor = W,).place(x = 10, y = 70)
        self.tb_valor = Entry(self)
        self.tb_valor.place(x=10, y=90)

