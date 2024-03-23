#Vamos personalizar a tela do aplicativo
#Vamos mudar a cor para verde - forma 1 passando o nome da cor
import flet as ft
def main(page:ft.Page):
    #page é o aplicativo como um tudo
    #vamos alterar a cor do plano de fundo
    #Como trabalhar com cores
    #Primeira forma:
    page.bgcolor = "green"
    page.update()
ft.app(target=main)