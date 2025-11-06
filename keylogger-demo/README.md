# Keylogger Demo (pseudocódigo e explicação)

> AVISO: esta seção explica como um keylogger funciona apenas para fins educacionais. O código público está **sanitizado** e não captura teclas.

## Pseudocódigo do keylogger real (para fins de estudo)
1. Iniciar listener do teclado (ex.: usando `pynput.keyboard.Listener`).
2. Para cada evento `on_press`:
   - Se for tecla imprimível, gravar `key.char` no buffer.
   - Se for tecla especial (space, enter, tab), gravar caractere substituto (`" "`, `"\n"`, `"\t"`).
   - Ignorar teclas de modificação (shift, ctrl, alt) conforme necessário.
3. Periodicamente, persistir o buffer em um arquivo `log.txt`.
4. Opcional: compactar/encriptar o log antes de exfiltrar (não incluído no demo).
5. Listener roda em background até ser interrompido.

## Observações
- Não inclua logs reais contendo senhas ou informações pessoais em repositórios.
- Para demonstração, usamos `keylogger_demo_safe.py` que gera entradas fictícias no `Keylogger/log.txt`.
