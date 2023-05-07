import PySimpleGUI as sg

def cadastrar ():
    #layout
    layout =[
        [sg.Text('Usuário',size=(7,0)),sg.Input(key='usuario',size=(20,1))],
        [sg.Text('Senha',size=(7,0)),sg.Input(key='senha',password_char='*',size=(20,1))],
        [sg.Button('Cadastrar',size=(7,0))],
        [sg.Text('',key='mensagem')]
    ]
    #Janela
    janela = sg.Window('Cadastro',layout)

    #Ler os eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        
        if eventos == 'usuario' == '':
                print('não digitou usuario')
        else:
            janela['mensagem'].update('Cadastro feito com sucesso')

            





