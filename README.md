# Projeto — Simulação de Ransomware e Keylogger em Python

**Desafio DIO – Ransomware e Keylogger em Python**

---

> ⚠️ **Aviso Importante**
> Este repositório foi desenvolvido **exclusivamente para fins educacionais**, em **ambiente 100% controlado e seguro**.
> **NÃO** execute estes scripts em máquinas de produção, redes corporativas ou sistemas de terceiros. O uso indevido é ilegal e antiético. O objetivo é aprender a se defender — nunca atacar.

---

## Visão Geral

Este repositório faz parte de um desafio prático do curso da **Digital Innovation One (DIO)** na área de **Cibersegurança**.
O projeto demonstra, de forma controlada, o funcionamento de dois tipos de malware:

* 🔐 **Ransomware** — criptografa arquivos de teste e simula um pedido de resgate.
* ⌨️ **Keylogger** — captura (simulado) das teclas digitadas e registra em um arquivo de log.

Todos os testes descritos aqui foram realizados em ambiente local e isolado (VSCode + diretório de teste). **Nenhum sistema real foi comprometido.**

---

## Objetivos de Aprendizagem

* Entender o comportamento técnico de malwares (ransomware e keylogger).
* Simular, de forma ética, ataques controlados usando Python.
* Desenvolver habilidades práticas em segurança ofensiva e defensiva.
* Documentar o projeto no GitHub como portfólio técnico.

---

## Estrutura do Projeto

```

│── ransomware-demo/
│      ├── ransomware_demo_safe.py        # versão sanitizada (modo --dry-run / --confirm)
│      └── descriptografar_demo_safe.py   # versão sanitizada de recuperação
│── keylogger-demo/
│       ├── keylogger_demo_safe.py         # versão simulada (gera entradas fictícias)
│       └── README.md                       # explicação e pseudocódigo do keylogger real
│
├── Keylogger/
│   └── log.txt                             # exemplo de log (fictício)
│
├── samples/
│   └── test_files/
│       ├── dados_confidencias.txt
│       └── senhas.txt
│
├── docs/
│   └── relatorio.md
├── README.md
├── LICENSE
└── .gitignore
```

> **Observação:** os scripts públicos aqui são **sanitizados** — evitam captura real e operam somente sobre `samples/test_files/` ou geram entradas fictícias no log. Leia os README de cada demo antes de executar.

---

## Ransomware (simulado)

**Arquivo (exemplo):** `ransomware-demo/ransomware_demo_safe.py`

Descrição curta:

* Gera uma chave local de demonstração (`chave_demo.key`).
* Percorre `samples/test_files/` e (simula) criptografa os arquivos.
* Cria `LEIA-ME-DEMO.txt` com mensagem de resgate contendo *placeholders* (`PLACEHOLDER_BTC_ADDR`, `PLACEHOLDER_EMAIL`).

**Modo seguro:**

* `--dry-run` — simula operações sem modificar arquivos.
* Para executar sem dry-run, o demo exige `--confirm` para evitar execução acidental.

**Fluxo resumido:**

1. Gerar chave (Fernet).
2. Buscar arquivos em `samples/test_files/` (ignorando chaves e scripts).
3. Encriptar (ou simular) e sobrescrever arquivos de teste.
4. Criar arquivo de instruções (simulado).

O script de descriptografia (`descriptografar_demo_safe.py`) faz o processo inverso usando a chave demo.

---

## Keylogger (simulado)

**Arquivo (exemplo):** `keylogger-demo/keylogger_demo_safe.py`
**Log de exemplo:** `Keylogger/log.txt`

Descrição curta:

* Explica o funcionamento real do keylogger por *pseudocódigo* no `keylogger-demo/README.md`.
* A versão pública **não** usa `pynput`; em vez disso gera entradas fictícias com timestamp para demonstrar o formato do log.

Recursos demonstrados:

* Como seriam tratados caracteres imprimíveis e teclas especiais (Enter, Espaço, Tab).
* Escrita contínua em `log.txt`.
* Observações sobre furtividade e riscos (documentadas no README do demo).

---

## Tecnologias

* Python 3
* `cryptography` (Fernet) — demonstração de criptografia simétrica
* `pynput` — usado apenas na explicação/pseudocódigo (não no código público)
* VSCode — ambiente de desenvolvimento

---

## Ambiente de Teste (recomendações)

* Use uma **VM isolada** (VirtualBox/VMware) com snapshot antes de qualquer execução.
* Preferencial executar sem rede (ou com rede bloqueada).
* Trabalhe apenas com arquivos em `samples/test_files/`.
* Sempre começar com `--dry-run` nas demos que oferecem essa opção.
* Não publique logs com dados reais; mantenha apenas exemplos fictícios.

---

## Boas Práticas e Defesa (resumo)

Ao trabalhar com ameaças e simulações, priorize:

* Backup offline e testado;
* EDR/antivírus com heurísticas comportamentais;
* Least privilege e segmentação de rede;
* Treinamento e conscientização sobre phishing;
* Políticas de resposta a incidentes e recuperação.

---

## Exemplo de log (fictício)

```
[2025-11-05 10:12:03] Captured: ola boa tarde
[2025-11-05 10:12:05] Captured: senha123
[2025-11-05 10:12:11] Captured: teste de gravação
```

> **Importante:** nunca inclua registros com senhas reais ou dados sensíveis em repositórios públicos.

---

## Conclusão

Este projeto fornece uma visão prática sobre como **ransomware** e **keyloggers** operam, com foco em **entendimento e defesa**. Saber como o ataque funciona é essencial para construir melhores mecanismos de proteção.

> “Conhecer o ataque é o primeiro passo para construir a defesa.”

---

## Autor

**Vitor Lopes Fernandes de Souza**
Estudante e entusiasta em Cibersegurança — foco em Pentest e Segurança da Informação

---

## Licença

Licenciado sob **MIT License** — uso livre para fins educacionais.
Por favor, **não utilize** o código de forma maliciosa.
