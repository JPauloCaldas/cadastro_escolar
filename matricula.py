from tkinter import *
from tkinter import ttk
from main import *


def validate_entry2(text):
    if text == "":
        return True
    try:
        value = int(text)
    except ValueError:
        return False
    return 0 <= value <= 100


class Toplavelmatricula(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.vcmd_cpf = (self.register(validate_cpf), '%P')
        list_class = ['INFANTIL 2', 'INFANTIL 3', 'INFANTIL 4', 'INFANTIL 5']

        self.title('MATRÍCULA DE ALUNO')
        self.geometry('1100x500+200+200')

        font_label = ("Helvetica", 14)
        font_entry = ("Helvetica", 14)
        font_title = ("Times New Roman", 20, "bold")


        self.lb_title = Label(self, text='REGISTRO DE MATRICULA', anchor=W, font=font_title)
        self.lb_title.place(x=9, y=5)

        # Posicionamento dos widgets do lado esquerdo
        self.lb_name = Label(self, text='Nome do Aluno', anchor=W, font=font_label)
        self.lb_name.place(x=10, y=60)
        self.tb_name = Entry(self, width=50, font=font_entry)
        self.tb_name.place(x=10, y=85)

        self.lb_age = Label(self, text='Data de Nascimento', anchor=W, font=font_label)
        self.lb_age.place(x=10, y=120)
        self.tb_age = Entry(self, font=font_entry)
        self.tb_age.place(x=10, y=145)

        self.lb_address = Label(self, text='Endereco', anchor=W, font=font_label)
        self.lb_address.place(x=10, y=180)
        self.tb_address = Entry(self, width=50, font=font_entry)
        self.tb_address.place(x=10, y=205)

        self.lb_class = Label(self, text='Turma', anchor=W, font=font_label)
        self.lb_class.place(x=10, y=240)
        self.tb_class = ttk.Combobox(self, values=list_class, font=font_entry)
        self.tb_class.place(x=10, y=265)

        self.lb_parents = Label(self, text='Responsável', anchor=W, font=font_label)
        self.lb_parents.place(x=10, y=300)
        self.tb_parents = Entry(self, width=50, font=font_entry)
        self.tb_parents.place(x=10, y=325)

        # Posicionamento dos widgets do lado direito
        self.lb_fone = Label(self, text='Telefone', anchor=W, font=font_label)
        self.lb_fone.place(x=700, y=60)
        self.tb_fone = Entry(self, validate="key", validatecommand=self.vcmd_cpf, font=font_entry)
        self.tb_fone.place(x=700, y=85)

        self.lb_email = Label(self, text='Email', anchor=W, font=font_label)
        self.lb_email.place(x=700, y=120)
        self.tb_email = Entry(self, font=font_entry)
        self.tb_email.place(x=700, y=145)

        self.lb_whatsapp = Label(self, text='WHATSAPP', anchor=W, font=font_label)
        self.lb_whatsapp.place(x=700, y=180)
        self.tb_whatsapp = Entry(self, validate="key", validatecommand=self.vcmd_cpf, font=font_entry)
        self.tb_whatsapp.place(x=700, y=205)

        self.lb_cpf = Label(self, text='CPF do Responsável', anchor=W, font=font_label)
        self.lb_cpf.place(x=700, y=240)
        self.tb_cpf = Entry(self, validate="key", validatecommand=self.vcmd_cpf, font=font_entry)
        self.tb_cpf.place(x=700, y=265)

        # Botão Matricular
        button_matricular = Button(self, text="Matricular", font=("Arial","20", "bold"), bg="#25c4f4", relief="solid", command=lambda: [
            Matricular(self.tb_name, self.tb_age, self.tb_address, self.tb_class, self.tb_parents, self.tb_fone, self.tb_email, self.tb_whatsapp, self.tb_cpf),
            LimparMatricula(self.tb_name, self.tb_age, self.tb_address, self.tb_class, self.tb_parents, self.tb_fone, self.tb_email, self.tb_whatsapp, self.tb_cpf)
        ])
        button_matricular.place(x=900, y=400)

