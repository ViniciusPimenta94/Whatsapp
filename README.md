# Automação de Mensagens no WhatsApp

Este projeto automatiza o envio de mensagens personalizadas via WhatsApp Web usando Python, Selenium e uma lista de contatos em Excel.

---

## 📦 Estrutura do Projeto

- `Whatsapp.py`: Script principal da automação que abre o WhatsApp Web, autentica via QR Code e envia mensagens personalizadas.
- `Contatos.xlsx`: Arquivo Excel com a lista de contatos e mensagens a serem enviadas.

---

## 🛠 Requisitos

- Python 3.x
- Navegador Google Chrome instalado
- Bibliotecas:
  - `pandas`
  - `selenium`
  - `urllib` (biblioteca padrão)
  - `webdriver-manager`

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

1. Certifique-se de que o Chrome está instalado.
2. Preencha o arquivo `Contatos.xlsx` com as colunas: `Pessoa`, `Número`, `Mensagem`.
3. Execute o script:

```bash
python Whatsapp.py
```

4. Escaneie o QR Code para autenticar no WhatsApp Web.
5. O script enviará as mensagens automaticamente para cada contato listado.

---

## ⚠️ Observações

- Os números devem estar no formato internacional (ex: `+5511999998888`).
- O script aguarda o carregamento da interface antes de enviar cada mensagem.
- O envio inclui um intervalo de 10 segundos por contato para evitar bloqueios.

---

## 📄 Licença

MIT
