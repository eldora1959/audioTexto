import os
import whisper

AUDIO_FILE = "audio.mp3"

if not os.path.exists(AUDIO_FILE):
    print(f"Erro: arquivo não encontrado: {AUDIO_FILE}")
else:
    print("Carregando o modelo...")
    model = whisper.load_model("base")

    print("Transcrevendo o áudio...")
    result = model.transcribe(
        AUDIO_FILE,
        language="pt"
    )

    texto = result["text"].strip()

    print("\nTexto reconhecido:")
    print(texto)

    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(texto)

    print("\nArquivo transcript.txt salvo com sucesso!")