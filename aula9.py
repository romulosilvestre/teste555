from regranegocio.cliente import Cliente
import flet as ft
def main(page:ft.Page):
    txt_nome = ft.TextField(label="nome",width=250)
    txt_data_nasc = ft.TextField(label="data de nascimento",width=250) 
    txt_cpf = ft.TextField(label="cpf",width=250)
    msg = ft.Text()
    def btn_click(e):       
        cliente = Cliente(txt_nome.value,txt_data_nasc.value,txt_cpf.value) 
        print(f"{cliente.get_nome()}-{cliente.get_data_nasc()}-{cliente.get_cpf()}")
    btn = ft.ElevatedButton("Cadastrar",
                            width=250,
                            color="black",on_click=btn_click)    
    page.add(txt_nome,txt_data_nasc,txt_cpf,btn,msg)    
ft.app(target=main)
