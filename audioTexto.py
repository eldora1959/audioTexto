
# Importa a biblioteca Whisper
import whisper

# Nome do arquivo de áudio que será transcrito
AUDIO_FILE = "audio.mp3"

# Carrega o modelo de reconhecimento de voz
model = whisper.load_model("base")

# Transcreve o áudio para texto
result = model.transcribe(AUDIO_FILE)

# Exibe o texto no terminal
print(result["text"])

# Salva a transcrição em um arquivo TXT
with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("\nTranscrição salva em transcript.txt")
