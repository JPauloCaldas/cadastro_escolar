from tkinter import *
from tkinter import ttk
import Banco
from main import*





    

class ToplavelRemover(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Escola Universo do ABC')
        self.geometry('1100x600')
        self.configure(background="#DCDCDC")



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



        self.frame1 = LabelFrame(self, relief="groove")
        self.frame1.pack(fill="both",side="top", expand= "yes", padx=10, pady=10)

        
        self.frame_treeview = Frame(self.frame1, relief="sunken")
        self.frame_treeview.pack(side='top', fill= "both", expand= "yes", padx=10, pady=5)

        self.frame_pesquisa = Frame(self.frame_treeview) #Frame da pesquisa
        self.frame_pesquisa.pack(side='bottom', fill= "both", expand= "yes", padx=10, pady=5)

        self.frame2 = Frame(self,)
        self.frame2.pack(side="top", fill= "both", expand= "yes", padx=10, pady=50)



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




        


        self.titulo_aluno = Label(self.frame2, text = 'ID do Aluno', foreground='#000000', anchor = W,)
        self.titulo_aluno.pack(fill= "both", side="left")
        self.etid = Entry(self.frame2)
        self.etid.pack(side="left")

        self.bt = Button(self.frame2, text="Excluir", command=lambda: [DeletStudent(self.etid)])
        self.bt.pack(side="left")

        # TREEVIEW

        self.trv = ttk.Treeview(self.frame_treeview, columns=('id', 'nome', 'nascimento', 'endereco', 'turma', 'pais', 'telefone', 'email', 'whatsself', 'cpf'), show='headings')
        
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
        self.trv.column('whatsself', minwidth=0, width=100)
        self.trv.column('cpf', minwidth=0, width=100)
        self.trv.heading('id', text='ID')
        self.trv.heading('nome', text='NOME')
        self.trv.heading('nascimento', text='NASCIMENTO')
        self.trv.heading('endereco', text='ENDEREÇO')
        self.trv.heading('turma', text='TURMA')
        self.trv.heading('pais', text='PAIS')
        self.trv.heading('telefone', text='TELEFONE')
        self.trv.heading('email', text='EMAIL')
        self.trv.heading('whatsself', text='WHATSself')
        self.trv.heading('cpf', text='CPF')
        self.trv.pack()


