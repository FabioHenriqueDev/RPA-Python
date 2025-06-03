# 🤖 RPA: Automação de Envio de E-mails com PyAutoGUI + Pandas

Este projeto realiza uma automação completa com Python, utilizando técnicas de RPA (Robotic Process Automation). A aplicação acessa o Gmail automaticamente, faz o download da lista de contatos, lê os dados com Pandas e envia e-mails personalizados para cada contato da lista.

---

## 🔧 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) – automação da interface gráfica
- [Pandas](https://pandas.pydata.org/) – leitura e tratamento de dados
- [smtplib](https://docs.python.org/3/library/smtplib.html) – envio de e-mails via protocolo SMTP
- [time](https://docs.python.org/3/library/time.html) – controle de tempo entre ações
- [os](https://docs.python.org/3/library/pathlib.html) – variáveis de ambiente

---

## 🚀 Funcionalidades

- Abre o navegador e acessa o Gmail
- Faz o download dos contatos
- Lê o arquivo CSV gerado
- Percorre a coluna de email
- Envia um e-mail para cada pessoa da coluna

---