from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import Banco
from main import *

class Toplavelatualizar(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Escola')
        self.geometry('1050x600')

      

        
        #-----------------------------------------------------
        def ShowAll():
            vquery = "SELECT * FROM tb_students order by id"
            linha = Banco.dql(vquery)
            exibir_dados(linha)

                #Pesquisa alunos pelo nome

        def SelectStudenttxt():
            nome_aluno = self.tb_name.get()
            vquery = "SELECT * FROM tb_students WHERE NAME = ?"
            params = (nome_aluno,)
            resultado = Banco.dql(vquery, params)
            exibir_dados(resultado)

        #Pesquisa alunos pelo ID
        def SelectId():
            id_aluno = self.id.get()
            vquery = "SELECT * FROM tb_students WHERE id = ?"
            params = (id_aluno,)
            resultado = Banco.dql(vquery, params)
            exibir_dados(resultado)


        #Limpa o TreeView e mostra o novo resultado da busca
        def exibir_dados(dados):
            self.trv.delete(*self.trv.get_children())  # Limpar o Treeview antes de exibir os dados
            for row in dados:
                self.trv.insert('', 'end', values=row) #mostra o novo resultado da busca




        ################    FRAMES     #################

        # Frames Principas
        self.frame1 = LabelFrame(self, relief="groove")
        self.frame1.pack(fill="both",side="top", expand= "yes", padx=10, pady=10)

        self.frame2 = LabelFrame(self)
        self.frame2.pack(fill= "both", expand= "yes", padx=10, pady=10)


        ##### Dentro da Frame 1 #####
        self.frame_treeview = LabelFrame(self.frame1, relief="sunken") #Frame do TreeView
        self.frame_treeview.pack(fill= "both", expand= "yes", padx=10, pady=10)

        self.frame_pesquisa = Frame(self.frame1) #Frame da pesquisa
        self.frame_pesquisa.pack(fill= "both", expand= "yes", padx=10, pady=10) 





        #### Dentro da Frame 2 #####
        self.frame_id = LabelFrame(self.frame2, relief="flat")
        self.frame_id.pack(fill="both", side="top", expand= "yes", padx=1, pady=1)

        #Frames que dividem a Frame 2
        self.frame2a = LabelFrame(self.frame2)
        self.frame2a.pack(fill= "both", side="left", expand= "yes", padx=1, pady=5)

        self.frame_dow_a = LabelFrame(self.frame2a)
        self.frame_dow_a.grid(column=0, row=6, pady=70)

        self.frame2b = LabelFrame(self.frame2)
        self.frame2b.pack(fill= "both", side="left", expand= "yes", padx=1, pady=5)

        self.frame_dow_b = LabelFrame(self.frame2b)
        self.frame_dow_b.grid(column=0, row=6, pady=70)

        self.frame2c = LabelFrame(self.frame2)
        self.frame2c.pack(fill= "both", side="left", expand= "yes", padx=1, pady=5)

        self.frame_dow_c = LabelFrame(self.frame2c)
        self.frame_dow_c.grid(column=0, row=6, pady=70)


        #--------------WIDGETS DA FRAME 1 ------------------------------

        self.id = Label(self.frame_id, text= 'ID do Aluno')
        self.id.pack(side="left", padx=5)
        self.tb_id = Entry(self.frame_id)
        self.tb_id.pack(side="left", padx=5)

        self.orientacao = Label(self.frame_id, text='<--     LEMBRE DE INFORMAR O ID DO ALUNO NO CAMPO A ESQUEDA', font=("Times New Roman", 15, "bold"),foreground='red')
        self.orientacao.pack(side="left", padx=5)


        self.lb_nome = Label(self.frame_pesquisa, text='Nome do Aluno:') #PESQUISAR PELO NOME
        self.lb_nome.pack(side='left', padx=5)
        self.tb_name = Entry(self.frame_pesquisa, width=50)
        self.tb_name.pack(side='left', padx=5)
        self.bt_pesquisar_nome = Button(self.frame_pesquisa, text='Pesquisar', command=SelectStudenttxt)
        self.bt_pesquisar_nome.pack(side='left', padx=5)



        self.lb_id = Label(self.frame_pesquisa, text='ID do Aluno:') #PESQUISAR PELO ID
        self.lb_id.pack(side='left', padx=5)
        self.id = Entry(self.frame_pesquisa)
        self.id.pack(side='left', padx=5)
        self.bt_pesquisar_id = Button(self.frame_pesquisa, text='Pesquisar', command=SelectId)
        self.bt_pesquisar_id.pack(side='left', padx=5)



        self.bt_showall = Button(self.frame_pesquisa, text='Mostrar Todos', command=ShowAll) #MOSTRAR TODOS ALUNOS
        self.bt_showall.pack(side='right', padx=30)


        #-------------------------TREEVIEWS--------------------------------------

        self.trv = ttk.Treeview(self.frame_treeview, columns=('id', 'nome', 'nascimento', 'endereco', 'turma', 'pais', 'telefone', 'email', 'whatsapp', 'cpf'), show='headings')
        
        # Barra de rolagem Vertical
        self.barrav = Scrollbar(self.frame_treeview, orient="vertical", command=self.trv.yview)
        self.barrav.pack(side='right', fill='y')
        self.trv.configure(yscrollcommand=self.barrav.set)

        # Barra de rolagem Horizontal
        self.barrah = Scrollbar(self.frame_treeview, orient="horizontal", command=self.trv.xview)
        self.barrah.pack(side='bottom', fill='x')
        self.trv.configure(xscrollcommand=self.barrah.set)

        self.trv.column('id', minwidth=0, width=50)
        self.trv.column('nome', minwidth=0, width=250)
        self.trv.column('nascimento', minwidth=0, width=100)
        self.trv.column('endereco', minwidth=0, width=250)
        self.trv.column('turma', minwidth=0, width=80)
        self.trv.column('pais', minwidth=0, width=100)
        self.trv.column('telefone', minwidth=0, width=100)
        self.trv.column('email', minwidth=0, width=100)
        self.trv.column('whatsapp', minwidth=0, width=100)
        self.trv.column('cpf', minwidth=0, width=100)
        self.trv.heading('id', text='ID')
        self.trv.heading('nome', text='NOME')
        self.trv.heading('nascimento', text='NASCIMENTO')
        self.trv.heading('endereco', text='ENDEREÇO')
        self.trv.heading('turma', text='TURMA')
        self.trv.heading('pais', text='PAIS')
        self.trv.heading('telefone', text='TELEFONE')
        self.trv.heading('email', text='EMAIL')
        self.trv.heading('whatsapp', text='WHATSAPP')
        self.trv.heading('cpf', text='CPF')
        self.trv.pack()


        #--------------WIDGETS DA FRAME 2 ------------------------------



        # --------------- frame 2a ------------------------------
        # Nome
        self.newname = Label(self.frame2a, text = 'Novo Nome').grid(column=0, row=0, sticky='w')
        self.tb_newname = Entry(self.frame2a, width=40)
        self.tb_newname.grid(column=0, row=1, sticky='w', padx=5)
        self.bt_name = Button(self.frame2a, text="Atualizar", command=lambda: [AtualizarNome(self.tb_id,self.tb_newname)])
        self.bt_name.grid(column=1, row=1)
        
        # Idade
        self.newage = Label(self.frame2a, text = 'Idade').grid(column=0, row=2, sticky='w')
        self.tb_newage = Entry(self.frame2a, width=40)
        self.tb_newage.grid(column=0, row=3, sticky='w', padx=5)
        self.bt_age = Button(self.frame2a, text="Atualizar", command=lambda: [AtualizarIdade(self.tb_id, self.tb_newage)])
        self.bt_age.grid(column=1, row=3)

        # Endereço
        self.newaddress = Label(self.frame2a, text = 'Endereço').grid(column=0, row=4, sticky='w')
        self.tb_newaddress = Entry(self.frame2a, width=40)
        self.tb_newaddress.grid(column=0, row=5, sticky='w', padx=5)
        self.bt_address = Button(self.frame2a, text="Atualizar", command=lambda: [AtualizarEndereco(self.tb_id, self.tb_newaddress)])
        self.bt_address.grid(column=1, row=5)

        # --------------- frame 2b ------------------------------

        # Turma
        self.newclass = Label(self.frame2b, text = 'Turma').grid(column=0, row=0, sticky='w')
        self.tb_newclass = Entry(self.frame2b, width=40)
        self.tb_newclass.grid(column=0, row=1, sticky='w', padx=5)
        self.bt_class = Button(self.frame2b, text="Atualizar", command=lambda: [AtualizarTurma(self.tb_id, self.tb_newclass)])
        self.bt_class.grid(column=1, row=1)


        # Responsáveis
        self.newparents = Label(self.frame2b, text='Responsáveis').grid(column=0, row=2, sticky='w')
        self.tb_newparents = Entry(self.frame2b, width=40)
        self.tb_newparents.grid(column=0, row=3, sticky='w', padx=5)
        self.bt_parents = Button(self.frame2b, text="Atualizar", command=lambda: [AtualizarResponsaveis(self.tb_id, self.tb_newparents)])
        self.bt_parents.grid(column=1, row=3)

        # Telefone
        self.newfone = Label(self.frame2b, text='Telefone').grid(column=0, row=4, sticky='w')
        self.tb_newfone = Entry(self.frame2b, width=40)
        self.tb_newfone.grid(column=0, row=5, sticky='w', padx=5)
        self.bt_fone = Button(self.frame2b, text="Atualizar", command=lambda: [AtualizarTelefone(self.tb_id, self.tb_newfone)])
        self.bt_fone.grid(column=1, row=5)

        # --------------- frame 2c ------------------------------

        # Email
        self.newemail = Label(self.frame2c, text='Email').grid(column=0, row=0, sticky='w')
        self.tb_newemail = Entry(self.frame2c, width=40)
        self.tb_newemail.grid(column=0, row=1, sticky='w', padx=5)
        self.bt_newemail = Button(self.frame2c, text="Atualizar", command=lambda: [AtualizarEmail(self.tb_id, self.tb_newemail)])
        self.bt_newemail.grid(column=1, row=1)

        # Whatsapp
        self.newwhars = Label(self.frame2c, text='Whatsapp').grid(column=0, row=2, sticky='w')
        self.tb_newwhatsapp = Entry(self.frame2c, width=40)
        self.tb_newwhatsapp.grid(column=0, row=3, sticky='w', padx=5)
        self.bt_newwhatsapp = Button(self.frame2c, text="Atualizar", command=lambda: [AtualizarWhatsapp(self.tb_id, self.tb_newwhatsapp)])
        self.bt_newwhatsapp.grid(column=1, row=3)

        # CPF
        self.newcpf = Label(self.frame2c, text='CPF').grid(column=0, row=4, sticky='w')
        self.tb_newcpf = Entry(self.frame2c, width=40)
        self.tb_newcpf.grid(column=0, row=5, sticky='w', padx=5)
        self.bt_newcpf = Button(self.frame2c, text="Atualizar", command=lambda: [AtualizarCPFResponsaveis(self.tb_id, self.tb_newcpf)])
        self.bt_newcpf.grid(column=1, row=5)
