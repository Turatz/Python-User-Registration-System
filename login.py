import json
import os
import time
#sistema de login
with open('dados.json') as arquivo: #contas
    dados = json.load(arquivo)

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
def bloqueio():
    time.sleep(3)
def usuario():
    tentativas = 3

    while tentativas > 0:

        usuario_digitado = input('Digite seu usuario: ')

        for usuario in dados:
            if usuario_digitado == usuario['usuario']:
                print('Usuario correto!')
                return usuario
        else:
            tentativas -= 1
            print('Usuario errado!')
            print(f'Tentativas restantes: {tentativas}')

            if tentativas == 0:
                print('Acesso bloqueado!')
                bloqueio()
                return None #retorna nada
def senha(usuario):
    tentativas = 3

    while tentativas > 0:

        senha_digitado = input('Digite sua senha: ')

        if senha_digitado == usuario['senha']:
            print('Senha correta!')
            return True
        else:
            tentativas -= 1
            print('Senha errada!')
            print(f'Tentativas restantes: {tentativas}')

            if tentativas == 0:
                print('Acesso bloqueado!')
                bloqueio()
def mensagem():
    limpar()
    print('-'*20)
    print('Seja bem vindo')
    print('-'*20)
def email(usuario):
    tentativas = 3

    while tentativas > 0:

        email_digitado = input('Digite seu email: ')

        if email_digitado == usuario['email']:
            print('Email correto!')
            return True
        else:
            tentativas -= 1
            print('Email errado!')
            print(f'Tentativas restantes: {tentativas}')

            if tentativas == 0:
                print('Acesso bloqueado!')
                bloqueio()

def main():  # esqueleto
    limpar()

    usuario_encontrado = usuario()

    if usuario_encontrado:
        if senha(usuario_encontrado):
            if email(usuario_encontrado):
                mensagem()
if __name__ == '__main__':
    main()