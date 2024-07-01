import sqlite3
from sqlite3 import Error



pastaApp = "C:\\workspace\\python\\project_abc\\"
nomeBanco = pastaApp + "registro.db"

def ConexaoBanco():
    con = None
    try:
        con = sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def dql(query, params=None):  # select
    vcon = ConexaoBanco()
    c = vcon.cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res

def dml(query, params=None):  # insert, update, delete
    try:
        vcon = ConexaoBanco()
        c = vcon.cursor()
        if params:
            c.execute(query, params)
        else:
            c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
