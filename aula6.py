#Vamos personalizar a tela do aplicativo
#Vamos mudar a cor para verde - forma 1 passando o nome da cor
#Flet não aceita o tipo RGB apenas HEX (rexis)
import flet as ft
def main(page:ft.Page):
    #page é o aplicativo como um tudo
    #vamos alterar a cor do plano de fundo
    #Como trabalhar com cores
    #Primeira forma (que legal ficou tipo um verde pantone rs):
    page.bgcolor = "#B0CA88"
    #Para verificar cores pesquise o seguinte endereço:
    #https://color.adobe.com/pt/create/color-wheel
    page.update()
ft.app(target=main)