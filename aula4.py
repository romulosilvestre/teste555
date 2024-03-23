#NOTE - tela de login do PI
import flet as ft
def main(page:ft.Page):
    msg = ft.Text(color="red")

    img = ft.Image(
        src=f"icones/logo.png",
        width=150,
        height=150,        
        fit=ft.ImageFit.CONTAIN,
    )
    #TextField
    txt_usuario = ft.TextField(
        label="Usuário",
        width=180,
        height=40,
        border_width=2,
        border_color="black",
        color="black"
    )
    txt_senha = ft.TextField(
        label="Senha",
        width=180,
        height=40,
        border_width=2,
        border_color="black",
        color="black",
        password=True
    )

    def btn_click(e):
        u = txt_usuario.value
        s = txt_senha.value
        msg.value = f"o usuário: {u} tem a senha: {s}"
        page.update()

    btn = ft.ElevatedButton("ENTRAR",width=250,on_click=btn_click)
    page.add(img,txt_usuario,txt_senha,btn,msg)
    page.horizontal_alignment="CENTER"
    page.vertical_alignment="CENTER"
    page.bgcolor = "white"
    page.update()
ft.app(target=main)