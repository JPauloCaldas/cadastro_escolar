from customtkinter import *



def click():
    print('fazer login')

app = CTk()
app.title('LOGIN')
app.geometry('500x300+200+200')
app.configure(background="#DCDCDC")

lb_user = CTkLabel(app, text= 'Nome do Usuário')
lb_user.pack(padx=10, pady=3)

tb_user = CTkEntry(app, placeholder_text='Seu Nome')
tb_user.pack(padx=10, pady=3)

lb_password = CTkLabel(app, text= 'Senha')
lb_password.pack(padx=10, pady=3)

tb_password = CTkEntry(app, placeholder_text='Sua Senha', show='*')
tb_password.pack(padx=10, pady=3)


button = CTkButton(app, text='login', command=click)
button.pack(padx=10, pady=10)

app.mainloop()