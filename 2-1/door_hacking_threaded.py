import zipfile
import string
import time
from itertools import product
import threading
import queue
import sys

zip_path = 'emergency_storage_key.zip'
chars = string.ascii_lowercase + string.digits
max_length = 6
found = False
lock = threading.Lock()
password_queue = queue.Queue(maxsize=1000)  # 큐에 너무 많은 작업을 미리 안 넣도록 제한

def password_generator():
    for pwd_tuple in product(chars, repeat=max_length):
        yield ''.join(pwd_tuple)

def feeder():
    for pwd in password_generator():
        if found:
            break
        password_queue.put(pwd)

# 암호를 시도하는 스레드 함수
def worker():
    global found
    while not found:
        try:
            password = password_queue.get(timeout=1)
        except queue.Empty:
            continue

        try:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(pwd=bytes(password, 'utf-8'))
                with lock:
                    if not found:
                        found = True
                        print(f"\n✅ 비밀번호 해제 성공! → {password}")
                        with open("password.txt", "w", encoding="utf-8") as f:
                            f.write(password)
        except:
            pass
        password_queue.task_done()

def unlock_zip_threading(thread_count=8):
    start_time = time.time()
    print("멀티스레딩으로 암호 해제 시도 중...")

    # 피더 스레드: 비밀번호를 생성하고 큐에 넣음
    feeder_thread = threading.Thread(target=feeder)
    feeder_thread.start()

    # 워커 스레드 실행
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # 모든 워커 스레드가 종료될 때까지 대기
    for t in threads:
        t.join()

    elapsed = round(time.time() - start_time, 2)
    print(f"\n⏱️ 총 소요 시간: {elapsed}초")

if __name__ == '__main__':
    unlock_zip_threading(thread_count=8)