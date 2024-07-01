from tkinter import *
from tkinter import messagebox
import Banco



def validate_cpf(text):
    if text == "": return True
    try:
        value = int(text)
    except ValueError:
        return False
    return 0 <= value <= 100000000000



def MsgBox(msg):
    messagebox.showinfo(title= "ATENCAO", message= msg)


def Clean(text):
    text.delete(0, END)
    

    
    
def LimparMatricula(name, age, address, turma, parents,fone, email, whatsapp, cpf):
    name.delete(0, END)
    age.delete(0, END)
    address.delete(0,END)
    turma.delete(0,END)
    parents.delete(0,END)
    fone.delete(0,END)
    email.delete(0,END)
    whatsapp.delete(0,END)
    cpf.delete(0,END)
    


def Matricular(name, age, address, tbclass, parents, fone, email, whatsapp, cpf):
    if name.get() != "" and age.get() != "" and address.get() != "" and tbclass.get() != "" and parents.get() != "" and fone !="" and email !="" and whatsapp !="" and cpf !="" :
        vname = name.get()
        vage = age.get()
        vaddress = address.get()
        vclass = tbclass.get()
        vparents = parents.get()
        vfone = fone.get()
        vemail = email.get()
        vwhatsapp = whatsapp.get()
        vcpf = cpf.get()
        vquery = "INSERT INTO tb_students (NAME, AGE, ADDRESS, CLASS, PARENTS, FONE, EMAIL, WHATSAPP, CPF_PARENTS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (vname, vage, vaddress, vclass, vparents, vfone, vemail, vwhatsapp, vcpf)
        Banco.dml(vquery, params)
        MsgBox('Matrícula Realizada com sucesso')
        
    else:
        MsgBox('Algum Campo está em Branco')


def AtualizarAluno(al_id, nv_name):
    aluno_id = al_id.get()
    novo_nome = nv_name.get()
    vquery = "UPDATE tb_students SET NAME = ? WHERE id = ?"
    params = (novo_nome, aluno_id)
    Banco.dml(vquery, params)




# ATUALIZAR OS DADOS

def AtualizarNome(al_id, nv_name):
    aluno_id = al_id.get()
    novo_name = nv_name.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)

    if resultado != []:
        vquery = "UPDATE tb_students SET NAME = ? WHERE id = ?"
        params = (novo_name, aluno_id,)
        Banco.dml(vquery, params)
        MsgBox('Nome Atualizado Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")



def AtualizarIdade(al_id, nv_age):
    aluno_id = al_id.get()
    nova_idade = nv_age.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)

    if resultado != []:
        vquery = "UPDATE tb_students SET AGE = ? WHERE id = ?"
        params = (nova_idade, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('Idade Atualizada Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")



def AtualizarEndereco(al_id, nv_address):
    aluno_id = al_id.get()
    novo_endereco = nv_address.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)

    if resultado != []:
        vquery = "UPDATE tb_students SET ADDRESS = ? WHERE id = ?"
        params = (novo_endereco, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('endereço Atualizado Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")




def AtualizarTurma(al_id, nv_class):
    aluno_id = al_id.get()
    nova_turma = nv_class.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)

    if resultado != []:
        vquery = "UPDATE tb_students SET CLASS = ? WHERE id = ?"
        params = (nova_turma, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('Turma Atualizada Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")




def AtualizarResponsaveis(al_id, nv_parents):
    aluno_id = al_id.get()
    novos_responsaveis = nv_parents.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)

    if resultado != []:
        vquery = "UPDATE tb_students SET PARENTS = ? WHERE id = ?"
        params = (novos_responsaveis, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('Responsável Atualizado Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")




def AtualizarTelefone(al_id, nv_fone):
    aluno_id = al_id.get()
    novo_telefone = nv_fone.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)
    

    if resultado != []:
        vquery = "UPDATE tb_students SET FONE = ? WHERE id = ?"
        params = (novo_telefone, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('Telefone Atualizado Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")




def AtualizarEmail(al_id, nv_email):
    aluno_id = al_id.get()
    novo_email = nv_email.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)
    

    if resultado != []:
        vquery = "UPDATE tb_students SET EMAIL = ? WHERE id = ?"
        params = (novo_email, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('E-mail Atualizado Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")




def AtualizarWhatsapp(al_id, nv_whatsapp):
    aluno_id = al_id.get()
    novo_whatsapp = nv_whatsapp.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)
    

    if resultado != []:
        vquery = "UPDATE tb_students SET WHATSAPP = ? WHERE id = ?"
        params = (novo_whatsapp, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('WhatsApp Atualizado Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")




def AtualizarCPFResponsaveis(al_id, nv_cpf_parents):
    aluno_id = al_id.get()
    novo_cpf_responsaveis = nv_cpf_parents.get()
    vquery = "SELECT * FROM tb_students WHERE id = ?"
    params = (aluno_id,)
    resultado = Banco.dql(vquery, params)
    

    if resultado != []:
        vquery = "UPDATE tb_students SET CPF_PARENTS = ? WHERE id = ?"
        params = (novo_cpf_responsaveis, aluno_id)
        Banco.dml(vquery, params)
        MsgBox('WhatsApp Atualizado Com Sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")



def DeletStudent(al_id):
    id = al_id.get()
    query_select = "SELECT * FROM tb_students WHERE id = ?" 
    id_select = (id,)
    resultado = Banco.dql(query_select, id_select)

    if resultado != []:
        vquery = "DELETE FROM tb_students WHERE id = ?"
        Banco.dml(vquery, (id,))
        MsgBox('Cadastro de Aluno removido com sucesso')
    else:
        MsgBox("                  ID NÃO ENCONTRADO!\nO campo 'ID do Aluno' precisa ser preenchido")

