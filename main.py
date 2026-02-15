import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import wave
import whisper
import os
import threading
import datetime
import sys
from PIL import Image, ImageTk   # para usar ícones .ico nos labels

# Função para localizar recursos mesmo dentro do .exe
def resource_path(relative_path):
    """Retorna o caminho correto do recurso, mesmo dentro do .exe"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Configuração do ffmpeg interno
os.environ["PATH"] += os.pathsep + os.path.abspath("bin")

# Modelo mais preciso
model = whisper.load_model("small")

samplerate = 44100
recording = False
paused = False
audio_chunks = []

def format_time(seconds):
    """Converte segundos em mm:ss"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02}:{secs:02}"

def record_loop(duration=None):
    global recording, paused, audio_chunks
    audio_chunks = []
    start_time = datetime.datetime.now()
    elapsed = 0

    while recording:
        if paused:
            continue

        chunk = sd.rec(int(1 * samplerate), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()
        audio_chunks.append(chunk)

        elapsed = (datetime.datetime.now() - start_time).seconds
        status_label.config(text=f"🎙️ Gravando... {format_time(elapsed)}")
        progress_bar["value"] = elapsed
        root.update()

        if duration and elapsed >= duration:
            stop_recording()
            break

def start_recording():
    global recording, paused
    try:
        duration = int(duration_entry.get())
    except ValueError:
        duration = None
    recording = True
    paused = False
    progress_bar["value"] = 0
    status_label.config(text="🎙️ Gravação iniciada")
    threading.Thread(target=record_loop, args=(duration,), daemon=True).start()

def pause_recording():
    global paused
    paused = not paused
    if paused:
        status_label.config(text="⏸️ Gravação pausada")
    else:
        status_label.config(text="▶️ Gravação retomada")
    root.update()

def stop_recording():
    global recording, audio_chunks
    recording = False
    status_label.config(text="⏹️ Gravação concluída")
    root.update()

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = datetime.datetime.now().strftime("%d-%m_%H%M")
    output_folder = os.path.join(desktop, f"Grav-{timestamp}")
    os.makedirs(output_folder, exist_ok=True)

    audio_file = os.path.join(output_folder, "Áudio Gravado.wav")
    txt_file = os.path.join(output_folder, "Transcrição do Áudio.txt")

    with wave.open(audio_file, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(b''.join([c.tobytes() for c in audio_chunks]))

    threading.Thread(target=transcribe_audio, args=(audio_file, txt_file, output_folder), daemon=True).start()

def transcribe_audio(audio_file, txt_file, output_folder):
    status_label.config(text="📝 Transcrevendo...")
    root.update()

    result = model.transcribe(audio_file, fp16=False, language="pt")
    transcription = result['text']

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, transcription)

    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(transcription)

    status_label.config(text=f"✅ Arquivos salvos em: {output_folder}")
    root.update()

# Interface Tkinter
root = tk.Tk()
root.title("🎧 Gravador e Transcritor de Áudio")
root.geometry("650x550")
root.configure(bg="#eaf6ff")  # fundo azul claro

# Ícone da janela (canto superior esquerdo)
try:
    root.iconbitmap(resource_path("microfone.ico"))
except:
    pass

status_label = tk.Label(root, text="Pronto para gravar", font=("Arial", 14, "bold"), bg="#eaf6ff")
status_label.pack(pady=15)

# Carregar ícone .ico para o Label
ico_img = Image.open(resource_path("time-tracking.ico"))   # usa resource_path
ico_img = ico_img.resize((24, 24))          
icon_tk = ImageTk.PhotoImage(ico_img)

# Label com ícone + texto
duration_label = tk.Label(
    root,
    image=icon_tk,
    text="Tempo de gravação (segundos, opcional):",
    compound="left",   # ícone à esquerda do texto
    font=("Arial", 12),
    bg="#eaf6ff"
)
duration_label.image = icon_tk  # evita descarte da imagem
duration_label.pack()

duration_entry = tk.Entry(root, width=10, font=("Arial", 12))
duration_entry.insert(0, "")
duration_entry.pack(pady=5)

# Botões estilizados
start_button = tk.Button(root, text="🎙️ Iniciar Gravação", command=start_recording,
                         bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20, height=2)
start_button.pack(pady=8)

pause_button = tk.Button(root, text="⏸️ Pausar / Retomar", command=pause_recording,
                         bg="#FFC107", fg="black", font=("Arial", 12, "bold"), width=20, height=2)
pause_button.pack(pady=8)

stop_button = tk.Button(root, text="⏹️ Encerrar Gravação", command=stop_recording,
                        bg="#F44336", fg="white", font=("Arial", 12, "bold"), width=20, height=2)
stop_button.pack(pady=8)

progress_bar = ttk.Progressbar(root, length=400, mode="determinate")
progress_bar.pack(pady=15)

text_box = tk.Text(root, height=12, width=70, font=("Arial", 11))
text_box.pack(pady=15)

root.mainloop()
