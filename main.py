from usuario import *
from classeproduto import *
from carrinho import *

def main():
    usuario_admin_padrao = Usuario("01", "admin", "admin@gmail.com","admin", "Administrador")

    print("=== TELA DE LOGIN ===")
    usuario_informado = input("Insira seu usuario para autenticação: ")
    senha_informada = input("Digite sua senha para autenticação: ")

    if usuario_informado == usuario_admin_padrao.nome and usuario_admin_padrao.autenticar(senha_informada): 
        print(" Login efetuado com sucesso!") 
    else: 
        print(" Usuário ou senha incorretos.")

    usuario_admin_padrao.alterar_senha("baleia")
    print(usuario_admin_padrao.obter_dados_perfil())

if __name__ == "__main__":
    main()
