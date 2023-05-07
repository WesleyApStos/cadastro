import PySimpleGUI as sg
import cadastro




#layout
layout =[
    [sg.Text('Usuário',size=(7,0)),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha',size=(7,0)),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Button('Cadastrar',size=(7,0)),sg.Button('Entrar',size=(7,0))],

    [sg.Text('',key='mensagem')]
]
#Janela
janela = sg.Window('Tela de Login',layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Entrar':
        janela['mensagem'].update('Logando')
    
    elif eventos == 'Cadastrar':
       cadastro.cadastrar()
       # ['mensagem'].update('Vamos cadastrar')