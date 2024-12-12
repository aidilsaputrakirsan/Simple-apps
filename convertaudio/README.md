# Simple Audio Transcription App

Aplikasi sederhana ini mengkonversi sebuah file audio (MP3) ke format WAV, kemudian mentranskripsinya ke teks menggunakan layanan Google Speech Recognition API.

## Fitur

- Mengkonversi audio MP3 ke WAV (mono, 16kHz) secara otomatis
- Melakukan transkripsi bahasa Indonesia (dapat disesuaikan ke bahasa lain)
- Menyimpan hasil transkripsi ke dalam file teks

## Persyaratan Sistem

- Python 3.x
- Koneksi internet (untuk mengakses Google Speech Recognition API)
- ffmpeg terinstal pada sistem Anda (untuk konversi audio)

## Instalasi

### Menginstal ffmpeg

#### Windows
1. Menggunakan Chocolatey:   ```bash
   choco install ffmpeg   ```
   
2. Atau download manual:
   - Kunjungi https://ffmpeg.org/download.html
   - Download versi Windows
   - Ekstrak file zip
   - Tambahkan path ffmpeg ke Environment Variables

#### macOS
Menggunakan Homebrew:

1. Kloning repository:   ```bash
   git clone https://github.com/username/simple-apps.git
   cd simple-apps   ```

2. Instal dependensi Python:   ```bash
   pip install -r requirements.txt   ```

## Cara Menggunakan

1. Letakkan file audio MP3 yang ingin ditranskripsi ke dalam folder `input_audio`. 
   Contoh: `input_audio/Storytelling-contoh.mp3`

2. Jalankan perintah berikut:   ```bash
   python script.py   ```

3. Skrip akan melakukan:
   - Konversi `input_audio/Storytelling-contoh.mp3` ke `output/Storytelling.wav`
   - Merekam suara 20 detik audio mulai dari offset 1 detik
   - Mengirimkan data audio ke Google Speech Recognition API
   - Menyimpan hasil transkripsi di `output/transcription.txt`

## Kustomisasi

- **Mengganti Nama File Input**: Ubah nilai `audio_file` di `script.py`
- **Durasi dan Offset**: Ubah parameter `duration` dan `offset` pada `recognizer.record()`
- **Bahasa Transkripsi**: Ubah parameter `language="id-ID"` pada `recognizer.recognize_google()` untuk bahasa lain (misal: `en-US` untuk Inggris)

## Troubleshooting

- Jika terjadi error Bad Request, pastikan koneksi internet Anda stabil
- Pastikan ffmpeg telah terinstal dan dapat dijalankan dari command line
- Jika audio terlalu panjang atau sulit dipahami, coba potong durasi atau gunakan audio yang lebih bersih

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.