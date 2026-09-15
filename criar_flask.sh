#!/usr/bin/env bash
set -e

echo "============================================================"
echo "        CRIADOR DE PROJETO FLASK COM UV (CODESPACES)"
echo "============================================================"
echo

# --- Instalar UV ---
echo "[1/4] Verificando instalacao do UV..."
if ! command -v uv &> /dev/null; then
    echo "UV nao encontrado. Instalando..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "UV ja esta instalado!"
fi

# --- UV Init na raiz ---
echo
echo "[2/4] Inicializando projeto com UV na raiz..."
uv init

# --- Instalar Flask ---
echo
echo "[3/4] Instalando Flask via UV..."
uv add flask

# --- Criar arquivos do projeto ---
echo
echo "[4/4] Criando arquivos do projeto..."

cat > main.py << 'EOF'
# Atalho no VS Code: Ctrl+Shift+B roda o Flask com debug (uv run flask --app main run --debug)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Renderiza a pagina principal."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
EOF

mkdir -p templates

cat > templates/index.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Flask App</title>
</head>
<body>
    <h1>Ola, mundo!</h1>
</body>
</html>
EOF

# --- Criar .gitignore ---
cat > .gitignore << 'EOF'
# Ambiente virtual do uv
.venv/

# Cache do Python
__pycache__/
*.py[cod]

# Variaveis de ambiente
.env

# Cache do uv
.uv_cache/
EOF

# --- Atalho no VS Code: Ctrl+Shift+B roda o Flask ---
mkdir -p .vscode

cat > .vscode/tasks.json << 'EOF'
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "UV Run Flask",
            "type": "shell",
            "command": "uv",
            "args": ["run", "flask", "--app", "main", "run", "--debug"],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": true,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": true
            },
            "problemMatcher": []
        }
    ]
}
EOF

echo
echo "============================================================"
echo "              PROJETO CRIADO COM SUCESSO!"
echo "============================================================"
echo "  main.py              = Aplicacao Flask com rota GET"
echo "  templates/index.html = Pagina com 'Ola, mundo!'"
echo "  .gitignore           = Ignora .venv, cache e .env"
echo "  .vscode/tasks.json   = Ctrl+Shift+B roda o Flask com debug"
echo "============================================================"
echo
