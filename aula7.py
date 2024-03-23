
import flet as ft
def main(page:ft.Page):
    #outra forma de usar sobre cores
    #Caso opte por usar o nome direto, você deve verificar
    #https://flet.dev/docs/guides/python/colors
    page.bgcolor = ft.colors.AMBER_900
    page.update()
ft.app(target=main)