#tupla - imutável  ()
#lista - mutável []
#dicionário - chave:valor {}
#passo 1 - criar a tupla
#passo 2 - percorrer a tupla
#passo 3 - adicionar na página cada item da tupla
import  flet as ft
def main(page:ft.Page):
    txt_usuario = ft.TextField()
    txt_senha = ft.TextField()
    #passo 1 - criar a tupla (imutável)
    tupla_equipes=('Marlon','Josian','Erika')
    #passo 2 - percorrer a tupla
    for item in tupla_equipes:
        #passo 3 - adicionar na página cada item da tupla
        page.add(ft.Text(item))
    
    page.add(txt_usuario,txt_senha)
    
ft.app(main)

