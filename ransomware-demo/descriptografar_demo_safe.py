"""
descriptografar_demo_safe.py
Versão segura do script de descriptografia que opera apenas sobre samples/test_files.
Requer o arquivo de chave em code/ransomware-demo/chave_demo.key (gerado pelo demo).
Tem modo --dry-run.
"""

import argparse
import os
from cryptography.fernet import Fernet

BASE_DIR = os.path.dirname(__file__)
SAMPLES_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "samples", "test_files"))
KEY_PATH = os.path.join(BASE_DIR, "chave_demo.key")

IGNORED_FILES = {"descriptografar_demo_safe.py", "chave_demo.key"}

def carregar_chave(path=KEY_PATH):
    with open(path, "rb") as f:
        return f.read()

def descriptografar_arquivo(arquivo, chave, dry_run=False):
    f = Fernet(chave)
    if dry_run:
        print("[DRY-RUN] Irá descriptografar:", arquivo)
        return
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)
    print("Descriptografado:", arquivo)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            if nome in IGNORED_FILES or nome.endswith(".key"):
                continue
            caminho = os.path.join(raiz, nome)
            lista.append(caminho)
    return lista

def main():
    parser = argparse.ArgumentParser(description="Descriptografar Demo (SANITIZED)")
    parser.add_argument("--dry-run", action="store_true", help="Simula ações sem modificar arquivos")
    args = parser.parse_args()

    if not os.path.exists(KEY_PATH):
        print("Arquivo de chave não encontrado em:", KEY_PATH)
        print("Execute o demo de criptografia (dry-run ou confirm) para gerar a chave de demonstração.")
        return

    chave = carregar_chave(KEY_PATH)
    arquivos = encontrar_arquivos(SAMPLES_DIR)
    if not arquivos:
        print("Nenhum arquivo encontrado em samples/test_files.")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave, dry_run=args.dry_run)

    print("Operação de descriptografia do demo concluída. (modo dry-run =", args.dry_run, ")")

if __name__ == "__main__":
    main()
