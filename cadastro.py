import os
import json
#sistema de cadastro
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

dados = []

def main():
    limpar()
    print('Crie sua conta!')
    print('-'*20)

    usuario = criar_usuario()
    senha = criar_senha()
    email = criar_email()
    mensagem()

    dados.append({
        'usuario': usuario,
        'senha': senha,
        'email': email
    })

    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def mensagem():
    limpar()
    print('-'*20)
    print('Conta criada com sucesso!')
    print('-'*20)

def criar_senha():
    limpar()
    senha_criada = input('Digite sua senha: ')
    return senha_criada

def criar_usuario():
    limpar()
    usuario_criado = input('Digite seu usuario: ')
    return usuario_criado

def criar_email():
    limpar()
    email_criado = input('Digite seu email: ')
    return email_criado

if __name__ == '__main__':
    main()