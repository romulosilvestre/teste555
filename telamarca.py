from regranegocio.marca import Marca
import flet as ft

def main(page:ft.Page):
    txt_nome = ft.TextField(label="nome",width=250)

    def btn_click(e):
        marca = Marca(txt_nome.value)
        print(f"nome:{marca.get_nome()}")
    btn = ft.ElevatedButton("Cadastrar",on_click=btn_click)
    page.add(txt_nome,btn)
ft.app(target=main)

