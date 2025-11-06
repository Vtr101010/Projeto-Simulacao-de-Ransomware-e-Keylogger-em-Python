"""
keylogger_demo_safe.py
Versão SANITIZADA do keylogger:
- Não utiliza pynput.
- Gera entradas fictícias para simular um log.
- Mantém um README que explica o funcionamento do keylogger real (pseudocódigo).
"""

import argparse
import os
import time
from datetime import datetime
import random

BASE_DIR = os.path.dirname(__file__)
LOG_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "Keylogger", "log.txt"))

SAMPLE_TEXTS = [
    "ola boa tarde",
    "senha123",
    "teste de gravação",
    "usuario: admin",
    "email: usuario@example.com"
]

def gerar_entrada_falsa():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto = random.choice(SAMPLE_TEXTS)
    return f"[{ts}] Captured: {texto}\n"

def append_log(path, entry, dry_run=False):
    if dry_run:
        print("[DRY-RUN] Iría acrescentar ao log:", entry.strip())
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(entry)

def main():
    parser = argparse.ArgumentParser(description="Keylogger Demo (SANITIZED)")
    parser.add_argument("--dry-run", action="store_true", help="Somente simula, não altera arquivos")
    parser.add_argument("--simulate-n", type=int, default=5, help="Quantidade de entradas fictícias")
    args = parser.parse_args()

    print("Keylogger Demo (SANITIZED). Log de exemplo:", LOG_PATH)
    for _ in range(args.simulate_n):
        entry = gerar_entrada_falsa()
        append_log(LOG_PATH, entry, dry_run=args.dry_run)
        time.sleep(0.2)

    print("Concluído. (modo dry-run =", args.dry_run, ")")

if __name__ == "__main__":
    main()
