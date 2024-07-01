from tkinter import *
import payment
import matricula
import consulta
import atualizar
import remove



class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('ESCOLA')
        self.geometry("1100x500+250+200")
        self.withdraw


        self.frame_logo = Frame(self, width="1100", height=50)
        self.frame_logo.grid(row=0, pady=0)
        self.lb_title = Label(self.frame_logo, text="SISTEMA DE GERENCIAMENTO ESCOLAR", font=("Times New Roman","25", "bold" ))
        self.lb_title.place(x=5, y=5)
        
        self.frame1 = Frame(self, width=1100, height=210)
        #self.frame1.pack(fill= "both", expand="yes", padx=10, pady=10)
        self.frame1.grid(row=2)

        self.frame2 = Frame(self, width=1100, height=240)
        #self.frame2.pack(fill= "both", expand= "yes", padx=10, pady=10)
        self.frame2.grid(row=3)




        self.bt_matricula = Button(self.frame1, text='Matrícular Aluno', font=("Arial","20", "bold"), bg="#25c4f4", relief="solid", height=3, command=self.Open_matricula)
        self.bt_matricula.place(x=70, y=70)

        self.bt_select = Button(self.frame1, text='Consultar \n dados \n Cadastrais', font=("Arial","20", "bold"), bg="#25c4f4", relief="solid", width=15, height=3, command=self.Open_consult)
        self.bt_select.place(x=410, y=70)

        self.bt_cancel = Button(self.frame1, text='Apagar Registro', font=("Arial","20", "bold"), bg="#25c4f4", relief="solid", height=3, command=self.Remover)
        self.bt_cancel.place(x=800, y=70)
        
        self.bt_payment = Button(self.frame2, text='Registrar Pagamento', font=("Arial","20", "bold"), bg="#25c4f4", relief="solid", height=3, command=self.Open_payment)
        self.bt_payment.place(x=190, y=50)

        self.bt_update = Button(self.frame2, text='Atualizar Cadastro', font=("Arial","20", "bold"), bg="#25c4f4", relief="solid", height=3, command=self.Atualizar)
        self.bt_update.place(x=600, y=50)

        

        self.toplevel_window = None

    def Open_payment(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = payment.Toplavelpayment(self) 
        else:
            self.toplevel_window.focus()
    
    def Open_matricula(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = matricula.Toplavelmatricula(self) 
        else:
            self.toplevel_window.focus()
    

    def Open_consult(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = consulta.Toplavelconsult(self) 
        else:
            self.toplevel_window.focus()



    def Atualizar(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = atualizar.Toplavelatualizar(self)
            else:
                self.toplevel_window.focus()


    def Remover(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = remove.ToplavelRemover(self)
        else:
            self.toplevel_window.focus()

app = App()

app.mainloop()
