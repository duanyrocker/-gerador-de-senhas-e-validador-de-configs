import string
import secrets
import hashlib
import requests
import json
import yaml
import os
from SmartSecurityPy import PasswordValidator


# -------------------------
# Função: Gerar Senha Forte
# -------------------------
def gerar_senha(tamanho, maiusculas, minusculas, qtd_digitos, especiais):
    total_requisitos = maiusculas + minusculas + qtd_digitos
    restante = tamanho - total_requisitos
    senha = []

    # Adiciona os requisitos obrigatórios
    senha += [secrets.choice(string.ascii_uppercase) for _ in range(maiusculas)]
    senha += [secrets.choice(string.ascii_lowercase) for _ in range(minusculas)]
    senha += [secrets.choice(string.digits) for _ in range(qtd_digitos)]

    # Preenche o restante com caracteres especiais escolhidos
    if especiais:  # só adiciona se o usuário não deixar vazio
        senha += [secrets.choice(especiais) for _ in range(restante)]
    else:
        # fallback: se não informar especiais, usa todos os símbolos
        senha += [secrets.choice(string.punctuation) for _ in range(restante)]

    secrets.SystemRandom().shuffle(senha)
    return ''.join(senha)


# -------------------------
# Função: Checar se a senha vazou
# -------------------------
def checar_senha_vazada(senha):
    sha1 = hashlib.sha1(senha.encode()).hexdigest().upper()
    prefixo = sha1[:5]
    sufixo = sha1[5:]

    url = f'https://api.pwnedpasswords.com/range/{prefixo}'
    resposta = requests.get(url)
    hashes_vazados = resposta.text.splitlines()

    for linha in hashes_vazados:
        hash_vazado, qtd = linha.split(':')
        if hash_vazado == sufixo:
            return int(qtd)
    return 0


# -------------------------
# Função: Validar Arquivo
# -------------------------
def validar_arquivo(caminho):
    if not os.path.exists(caminho):
        print("Arquivo não encontrado!")
        return False

    # Detecta extensão e tenta carregar
    try:
        if caminho.endswith('.json'):
            with open(caminho, 'r', encoding="utf-8") as f:
                dados = json.load(f)
        elif caminho.endswith(('.yaml', '.yml')):
            with open(caminho, 'r', encoding="utf-8") as f:
                dados = yaml.safe_load(f)
        else:
            print("Formato de arquivo não suportado!")
            return False
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return False

    problemas = []
    for chave, valor in dados.items():
        if 'senha' in chave.lower() and isinstance(valor, str):
            problemas.append(f"Campo '{chave}' não deve armazenar senha em plaintext!")

    if problemas:
        print("Problemas encontrados:")
        for p in problemas:
            print("-", p)
        return False
    else:
        print("Arquivo validado com sucesso! Nenhum problema encontrado.")
        return True


# -------------------------
# Menu Interativo
# -------------------------
def menu():
    while True:
        print("\n=== Segurança e Automação ===")
        print("1 - Gerar Senha Forte")
        print("2 - Validar Arquivo de Configuração")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            while True:
                exemplo_especiais = string.punctuation
                try:
                    tamanho = int(input("Digite o tamanho da senha desejada: "))
                    especiais = input(f"Digite quais caracteres especiais você quer na sua senha "
                                      f"(pressione Enter para usar padrão {exemplo_especiais}): ")
                    maiusculas = int(input("Digite quantas letras maiúsculas você quer na sua senha: "))
                    minusculas = int(input("Digite quantas letras minúsculas você quer na sua senha: "))
                    qtd_digitos = int(input("Digite quantos números você quer na sua senha: "))
                except ValueError:
                    print("Erro: insira apenas números nos campos de quantidade.")
                    continue

                total_requisitos = maiusculas + minusculas + qtd_digitos
                if total_requisitos > tamanho:
                    print("Erro: a soma dos requisitos excede o tamanho total da senha.")
                else:
                    break

            senha = gerar_senha(tamanho, maiusculas, minusculas, qtd_digitos, especiais)

            # Cria uma instância do validador
            validator = PasswordValidator()
            result = validator.validate_password(senha)

            print(f"\nSenha gerada: {senha}")
            print(f"Score: {result.score}")  # Pontuação de 0-100
            print(f"É forte? {result.is_strong}")  # True/False

            # Mostra feedback se existir
            if result.feedback:
                print("\n🔎 Feedback sobre a senha:")
                for f in result.feedback:
                    print("-", f)

            # Mostra sugestões específicas
            suggestions = validator.get_password_suggestions(senha)
            if suggestions:
                print("\n💡 Sugestões para melhorar:")
                for s in suggestions:
                    print("-", s)

            vazou = checar_senha_vazada(senha)
            if vazou:
                print(f"Atenção! Esta senha apareceu {vazou} vezes em vazamentos.")
            else:
                print("Senha segura e não encontrada em vazamentos!")

        elif escolha == "2":
            caminho = input("Digite o caminho do arquivo (.json ou .yaml): ")
            validar_arquivo(caminho)

        elif escolha == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# -------------------------
# Executar menu
# -------------------------
if __name__ == "__main__":
    menu()
