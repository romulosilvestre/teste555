#{Laboratório - Tela de Login}

#####Tela#####

import flet as ft
from login import Login
def main(page:ft.Page):  
       
    msg = ft.Text(color="white")
    txt_usuario = ft.TextField(
          label="Usuário",      
          width=250,
          height=50,
          border=1,
          border_color="white",
          color="white")
   
    txt_senha= ft.TextField(
        label="Senha",
        width=250,
        height=50,
        border=1,
        border_color="white",
        color="white",
        password=True)
     
    def btn_click(e):
        login = Login(txt_usuario.value,txt_senha.value)
        if login.valida_senha() == True:
            msg.value = "logou com sucesso"
        else:
            msg.value = "falha na autenticação"
        page.update()
    btn = ft.ElevatedButton("ENTRAR",
                            width=250,
                            on_click=btn_click)  
 
    
    page.add(txt_usuario,txt_senha,btn,msg)
    page.padding = 150
    page.horizontal_alignment= "CENTER"
    page.update()   

ft.app(target=main)

#######Regra de Negócio######

class Login:
    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha
        pass

    def valida_senha(self):
        if self.usuario == "Rômulo" and self.senha == "123":
            return True
        else:
            return False



'