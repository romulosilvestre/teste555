
import flet as ft
def main(page:ft.Page):
    #alinhamento
    
    page.add(ft.Text("Olá Mundo!"),          
             ft.Container(ft.Text(value="Olá Mundo",color="white"),bgcolor="black")
             )
    #vou esticar todos os elementos
    #START - padrão tudo a esquerda
    #STRECH - estica
    #CENTER - centraliza
    #END - ao final (direita)
    #SPACE_AROUND -espaçamento (espaço ao redor, calcula automáticamente)
    #SPACE_BETWEEN
    #SPACE_EVENLY 
    #page.spacing
    #page.padding
    page.title = "Curso Flet"  #nome do aplicativo 
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.padding = ft.padding.all(top=20,left=10,right=100,botton=50)
    page.update()
ft.app(target=main)