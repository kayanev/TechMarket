from flask import Flask, render_template, request

app = Flask(__name__)


# Classe feita por autoria de: Kayane Balielo
class Usuario:
    def __init__(self, id_usuario, nome, email, senha, tipo_permissao):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.tipo_permissao = tipo_permissao

    def autenticar(self, senha_informada):
        if not senha_informada:
            return False

        return self.__senha == senha_informada.strip()

    def alterar_senha(self, nova_senha):
        if nova_senha and len(nova_senha.strip()) > 0:
            self.__senha = nova_senha.strip()
            return True

        return False

    def obter_dados_perfil(self):
        return (
            f"Nome: {self.nome}\n"
            f"E-mail: {self.email}\n"
            f"Permissão: {self.tipo_permissao}"
        )

    def __repr__(self):
        return (
            f"<Usuario ID={self.id_usuario} "
            f"Nome='{self.nome}' "
            f"Permissao='{self.tipo_permissao}'>"
        )



usuario_admin_padrao = Usuario(
    "01",
    "admin",
    "admin@gmail.com",
    "admin",
    "Administrador"
)

#Rota feita por autroria de Manuela
@app.route("/", methods=["GET", "POST"])
def home():

    mensagem = ""
    sucesso = False

    if request.method == "POST":

        usuario_informado = request.form.get("usuario", "").strip()
        email_informado = request.form.get("email", "").strip()
        senha_informada = request.form.get("senha", "").strip()
        id_informado = request.form.get("id", "").strip()

        if (
            usuario_informado == usuario_admin_padrao.nome
            and email_informado == usuario_admin_padrao.email
            and senha_informada
            and usuario_admin_padrao.autenticar(senha_informada)
            and id_informado == usuario_admin_padrao.id_usuario
        ):
            mensagem = "Login efetuado com sucesso!"
            sucesso = True

        else:
            mensagem = "Usuário, e-mail, senha ou ID incorretos."

    return render_template(
        "index.html",
        mensagem=mensagem,
        sucesso=sucesso
    )


if __name__ == "__main__":
    app.run(debug=True)
