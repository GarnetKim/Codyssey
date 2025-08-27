import sounddevice as sd
import queue
import time
import numpy as np
from scipy.io.wavfile import write
from datetime import datetime
import os

# 🔧 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECORD_DIR = os.path.join(BASE_DIR, "records")

RECORD_SECONDS = 5
SAMPLE_RATE = 16000  # STT가 잘 되는 기본값
CHANNELS = 1  # 반드시 모노 채널

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

    # 현재 시간 기반 파일명 생성
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}.wav"
    filepath = os.path.join(RECORD_DIR, filename)

    # 파일 저장
    write(filepath, SAMPLE_RATE, audio_int16)
    print(f"✅ 녹음 완료: {filename}")
    return filepath

# 🟢 실행부
if __name__ == "__main__":
    record_audio()