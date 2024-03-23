#importando pacote - as(apelido)
import flet as ft
def main(page:ft.Page): #definição do objeto página
    #Text - título
    #TextField - caixa de texto
    #Button
    def click_btn1(e):
       btn2.disabled = False
       btn1.disabled = True
       page.update()
    
    #exercício - crie a mensagem funfou botão 1, botão 2....
    def click_btn2(e):
        btn1.disabled = False
        btn2.disabled = True   
        page.update()

    btn1 = ft.ElevatedButton("clique 1",on_click=click_btn1)
    btn2 = ft.ElevatedButton("clique 2",disabled=True,on_click=click_btn2)

    #Crie mais três botões nesse arquivo..:
      #execute desktop, execute web.
    page.add(btn1,btn2)   

ft.app(target=main)



