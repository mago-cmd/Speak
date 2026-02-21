# 🎧 Speak – Gravador e Transcritor de Áudio

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Whisper](https://img.shields.io/badge/Whisper-OpenAI-green)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![Status](https://img.shields.io/badge/status-em%20testes-yellow)

Um gravador de áudio com transcrição automática desenvolvido em **Python**.  
Ideal para entrevistas, reuniões ou estudos, permitindo gravar áudio e gerar transcrição em texto de forma simples.

---

##  Funcionalidades
- Interface gráfica feita com Tkinter.
- Botões para iniciar, pausar/retomar e encerrar gravações.
- Exibição do tempo decorrido e barra de progresso.
- Criação automática de pastas na Área de Trabalho para organizar gravações.
- Salvamento do áudio em `.wav` e da transcrição em `.txt`.
- Transcrição automática em português usando Whisper.

---

##  Bibliotecas utilizadas
- **tkinter / ttk** → Interface gráfica  
- **sounddevice** → Captura de áudio  
- **wave** → Salvamento em `.wav`  
- **whisper** → Transcrição automática  
- **os / datetime** → Manipulação de arquivos  
- **threading** → Execução paralela  
- **Pillow (PIL)** → Ícones `.ico`  

---

##  Como executar
```bash
# Clone o repositório
git clone https://github.com/seuusuario/gravador-transcritor.git

# Instale as dependências
pip install -r requirements.txt

# Execute o programa
python main.py
