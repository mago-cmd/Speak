# Speak


# Gravador e Transcritor de Áudio

Este projeto é um gravador de áudio com transcrição automática desenvolvido em Python.  
Ele permite gravar áudio do microfone, salvar em formato `.wav` e transcrever automaticamente para texto usando o modelo Whisper da OpenAI.

---

## Funcionalidades
- Interface gráfica feita com Tkinter.
- Botões para iniciar, pausar/retomar e encerrar gravações.
- Exibição do tempo decorrido e barra de progresso.
- Criação automática de pastas na Área de Trabalho para organizar gravações.
- Salvamento do áudio em `.wav` e da transcrição em `.txt`.
- Transcrição automática em português usando Whisper.
- Suporte a ícones `.ico` para estética da interface.

---

## Bibliotecas utilizadas
- **tkinter / ttk** → Interface gráfica.
- **sounddevice** → Captura de áudio do microfone.
- **wave** → Salvamento do áudio em `.wav`.
- **whisper** → Transcrição automática do áudio.
- **os / datetime** → Manipulação de arquivos e pastas.
- **threading** → Execução paralela (gravação e transcrição sem travar a interface).
- **Pillow (PIL)** → Exibição de ícones `.ico` nos labels.

---

## Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/gravador-transcritor.git

2. Instale as dependências
pip install -r requirements.txt

3. Execute o programa
python main.py


## Gerando o .exe
Este projeto inclui um arquivo .bat que automatiza a geração do executável .exe usando PyInstaller.
Isso permite rodar o programa em qualquer máquina Windows sem precisar ter o Python instalado.

1. Exemplo de comando usado no .bat:
pyinstaller --onefile --windowed main.py --icon=microfone.ico

--onefile → gera um único arquivo .exe.

--windowed → oculta o terminal ao rodar.

--icon → define o ícone do executável.

Após rodar o .bat, o .exe será gerado na pasta dist/.


## Estrutura de saída
Cada gravação gera uma pasta na Área de Trabalho com o nome:
Grav-DD-MM_HHMM

Dentro dela ficam:

Áudio Gravado.wav → arquivo de áudio.

Transcrição do Áudio.txt → transcrição automática.

## Status
Projeto funcional e pronto para uso.
Porem ainda em testes


## Observações
O modelo Whisper utilizado é o small, equilibrando precisão e desempenho.

É necessário ter o ffmpeg configurado (já incluído na pasta bin).

O .bat facilita a distribuição do programa como .exe.
