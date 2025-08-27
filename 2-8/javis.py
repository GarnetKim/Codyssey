import os
import queue
import time
import csv
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from scipy.io.wavfile import write
from datetime import datetime

# 🔧 설정
RECORD_SECONDS = 5
SAMPLE_RATE = 16000  # STT가 잘 되는 기본값
CHANNELS = 1  # 반드시 모노 채널
RECORD_DIR = "records"

os.makedirs(RECORD_DIR, exist_ok=True)

# 🎙️ 녹음 함수
def record_audio():
    print("🎙️ 녹음 시작...")
    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print("⚠️", status)
        q.put(indata.copy())

    audio_data = []

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='float32', callback=callback):
        start_time = time.time()
        while time.time() - start_time < RECORD_SECONDS:
            audio_data.append(q.get())

    audio_np = np.concatenate(audio_data, axis=0)

    # ✅ float32 → int16 변환
    audio_int16 = np.int16(audio_np * 32767)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}.wav"
    filepath = os.path.join(RECORD_DIR, filename)
    write(filepath, SAMPLE_RATE, audio_int16)
    print(f"✅ 녹음 완료: {filename}")
    return filepath

# 🧠 STT 변환 및 CSV 저장
def convert_audio_to_text(wav_path):
    recognizer = sr.Recognizer()

    print(f"🧠 STT 처리 중... ({os.path.basename(wav_path)})")
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language="ko-KR")
            print("✅ 인식된 텍스트:", text)

            csv_path = wav_path.replace(".wav", ".csv")
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["시간", "텍스트"])
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text])
            print(f"📁 CSV 저장 완료: {csv_path}")

        except sr.UnknownValueError:
            print("❌ 음성을 인식할 수 없습니다.")
        except sr.RequestError as e:
            print(f"❌ Google STT 요청 실패: {e}")

# 🟢 실행부
if __name__ == "__main__":
    wav_file = record_audio()
    convert_audio_to_text(wav_file)