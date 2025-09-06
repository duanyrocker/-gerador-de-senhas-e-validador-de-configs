````markdown
# 🔐 Segurança e Automação em Python

Este projeto é um **conjunto de ferramentas de segurança e automação** desenvolvido em Python.  
Ele inclui **duas funcionalidades principais**:

1️⃣ **Gerador de Senhas Fortes**  
- Gera senhas aleatórias com letras maiúsculas, minúsculas, números e símbolos.  
- Checa se a senha já apareceu em vazamentos usando a API **Have I Been Pwned**.  

2️⃣ **Validador de Arquivos de Configuração (JSON/YAML)**  
- Lê arquivos `.json` ou `.yaml`.  
- Detecta campos que armazenam **senhas em plaintext**.  
- Ajuda a manter **boas práticas de segurança** em arquivos de configuração.

---

## 💻 Tecnologias

- **Python 3.11+**  
- Bibliotecas:
  - `pyyaml` → leitura de arquivos YAML
  - `requests` → requisições HTTP
  - `secrets` → geração segura de senhas
  - `json` → leitura de arquivos JSON

---

## 📦 Instalação

1️⃣ Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd portfolio_segurança
````

2️⃣ Crie um ambiente virtual (opcional):

```bash
python -m venv venv
# Ativar
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

Execute o programa principal:

```bash
python main.py
```

Você verá o **menu interativo**:

```
=== 🔐 Segurança e Automação ===
1️⃣ - Gerar Senha Forte
2️⃣ - Validar Arquivo de Configuração
0️⃣ - Sair
```

### 1️⃣ Gerar Senha Forte

* Escolha a opção `1`.
* Informe o tamanho desejado da senha.
* ✅ O programa gera a senha e verifica se ela já vazou.

### 2️⃣ Validar Arquivo de Configuração

* Escolha a opção `2`.
* Informe o caminho do arquivo `.json` ou `.yaml`.
* ⚠️ O programa avisa se houver **senhas em plaintext**.

---

## 📂 Estrutura do Projeto

```
portfolio_segurança/
 ├── main.py             # Script principal com menu interativo
 ├── requirements.txt    # Dependências
 ├── README.md           # Este arquivo
 └── exemplos/           # Arquivos de teste
      ├── config.json
      └── config.yaml
```

---

## 📝 Exemplo de execução

**Gerador de senha:**

```
Senha gerada: 🔑 D7$fQk8&zB#1pA2!
Senha segura e não encontrada em vazamentos! ✅
```

**Validador de arquivo:**

```
Problemas encontrados ⚠️:
- Campo 'senha' não deve armazenar senha em plaintext!
```

---

## 🌟 Próximos passos / melhorias

* Suporte a arquivos **aninhados** (JSON/YAML dentro de objetos)
* Interface **colorida no terminal**
* Exportar relatórios de validação em **HTML ou PDF**
* Gerar **múltiplas senhas seguras** de uma vez

---

## 👩‍💻 Autor

**Duany Rocker**

* Analista de Segurança em Formação
* LinkedIn: [seu\_linkedin](https://www.linkedin.com/in/duanyrocker/)

```
