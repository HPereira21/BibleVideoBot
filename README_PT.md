[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)
[![Português](https://img.shields.io/badge/lingua-Português-green.svg)](README_PT.md)
# BibleVideoBot (Gerador Automático de Vídeos Devocionais com IA)

Gere vídeos devocionais automaticamente a partir de um versículo bíblico. Basta escrever algo como **"João 3:16"** ou **"Salmos 23:1"**, e o bot irá:

1. **Buscar o versículo** automaticamente (Português ou Inglês)
2. **Gerar um roteiro devocional** usando a API da OpenAI
3. **Criar o vídeo completo** com narração, vídeo de fundo e texto na tela
4. (Opcional) **Enviar para o YouTube** automaticamente

Ideal para canais de oração no WhatsApp, Instagram ou YouTube.

---

## 📁 Estrutura do Projeto

```
BibleVideoBot/
│
├── assets/               # Vídeos de fundo, música, imagens
├── output/               # Vídeos finais
├── temp/                 # Arquivos temporários
│
├── main.py               # Arquivo principal
├── video_engine.py       # Responsável pela criação do vídeo
├── uploader.py           # Responsável pelo upload no YouTube
├── script_generator.py   # NOVO — Busca o versículo e gera o roteiro
└── requirements.txt      # Dependências
```

---

## ⚙️ Instalação

### 1. Clone o Repositório

```
git clone https://github.com/yourusername/BibleVideoBot.git
cd BibleVideoBot
```

### 2. Instale o Python 3.10+ (Instruções para Windows mais abaixo)

Baixe aqui: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 3. Instale as Dependências

```
pip install -r requirements.txt
```

### 4. Adicione a sua OpenAI API Key

Edite o arquivo `script_generator.py` e substitua:

```
OPENAI_KEY = "YOUR_OPENAI_API_KEY_HERE"
```

Pela sua chave obtida em:
**[https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)**

---

## 🪟 Instruções Completas para Windows

### ✅ Passo 1 — Instalar Python

1. Baixe no site oficial
2. **IMPORTANTE:** marque a opção **“Add Python to PATH”**
3. Instale normalmente

### ✅ Passo 2 — Instalar FFmpeg (OBRIGATÓRIO)

Necessário para gerar o vídeo.

1. Baixe o FFmpeg:
   [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2. Extraia o zip (ex.: `C:\ffmpeg`)

3. Adicione ao PATH:

   * Win + R → `sysdm.cpl`
   * Aba **Avançado → Variáveis de Ambiente**
   * Em *Variáveis do Sistema*, selecione **Path** → Editar
   * Adicione:

     ```
     C:\ffmpeg\bin
     ```

4. Teste:

```
ffmpeg -version
```

Se aparecer a versão → OK.

### ✅ Passo 3 — Instalar Dependências

```
pip install -r requirements.txt
```

### ✅ Passo 4 — Adicionar a OpenAI Key

Edite o `script_generator.py`.

### Observação: Vozes TTS da Microsoft

No Windows elas já vêm instaladas.

---

## ▶️ Executando o Bot

Execute:

```
python main.py
```

1. Escolha o idioma/voz
2. Digite um versículo:

   * `Salmos 91:1`
   * `João 3:16`
3. O bot irá:

   * Buscar o texto bíblico
   * Gerar o roteiro devocional usando IA
   * Criar a narração
   * Gerar o vídeo final MP4

O vídeo será salvo em:

```
output/
```

Depois será perguntado:

```
Upload para o YouTube? (y/n)
```

Se escolher sim, o envio será automático.

---

## 💵 Custos

* **Bible API** → Grátis
* **OpenAI** → Muito barato

  * `gpt-4o-mini` custa centavos
* **Vozes (Edge TTS)** → Grátis no Windows

---

## ✨ Funcionalidades

* Multi-idioma (PT-BR e EN)
* Roteiros devocionais baseados em IA
* Vídeo totalmente automatizado
* Upload automático para YouTube
* Arquitetura modular e limpa

---

## 📌 Notas

* Coloque seus vídeos de fundo em `assets/`
* O envio ao YouTube requer autenticação na primeira execução

---

## 📜 Licença

MIT — livre para usar, modificar e distribuir.
