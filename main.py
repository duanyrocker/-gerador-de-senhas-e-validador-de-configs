import string
import secrets
import hashlib
import requests
import json
import yaml
import os


# -------------------------
# Função: Gerar Senha Forte
# -------------------------
def gerar_senha(tamanho=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha


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

    if caminho.endswith('.json'):
        with open(caminho, 'r') as f:
            dados = json.load(f)
    elif caminho.endswith('.yaml') or caminho.endswith('.yml'):
        with open(caminho, 'r') as f:
            dados = yaml.safe_load(f)
    else:
        print("Formato de arquivo não suportado!")
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
            tamanho = input("Digite o tamanho da senha (padrão 12): ")
            tamanho = int(tamanho) if tamanho.isdigit() else 12
            senha = gerar_senha(tamanho)
            print("Senha gerada:", senha)
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

