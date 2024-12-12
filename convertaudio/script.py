
import speech_recognition as sr
from pydub import AudioSegment
import os

# Path input dan output
audio_file = "input_audio/Storytelling-contoh.mp3"
converted_audio = "output/Storytelling.wav"

try:
    # Pastikan file input ada
    if not os.path.exists(audio_file):
        print("File input tidak ditemukan.")
        exit(1)

    # Konversi dengan set frame rate dan channels
    sound = AudioSegment.from_file(audio_file, format="mp3")
    sound = sound.set_frame_rate(16000).set_channels(1)

    # Pastikan folder output ada
    os.makedirs("output", exist_ok=True)

    sound.export(converted_audio, format="wav")
except Exception as e:
    print("Gagal mengkonversi audio:", e)
    exit(1)

if not os.path.exists(converted_audio) or os.path.getsize(converted_audio) == 0:
    print("File audio hasil konversi tidak ditemukan atau kosong.")
    exit(1)

recognizer = sr.Recognizer()

with sr.AudioFile(converted_audio) as source:
    print("Transcribing audio...")
    # Merekam audio 20 detik mulai dari detik ke-1 (ubah sesuai kebutuhan)
    audio_data = recognizer.record(source, duration=20, offset=1)

try:
    text = recognizer.recognize_google(audio_data, language="id-ID")
    print("Transcription:")
    print(text)
    with open("output/transcription.txt", "w", encoding="utf-8") as f:
        f.write(text)
except sr.RequestError as e:
    print("Terjadi masalah pada permintaan ke layanan Google:", e)
except sr.UnknownValueError:
    print("Google Speech Recognition tidak dapat memahami audio.")
except Exception as e:
    print("Error saat transkripsi:", e)
