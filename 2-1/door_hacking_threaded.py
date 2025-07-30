import zipfile
import string
import time
from itertools import product
import threading
import queue

zip_path = 'emergency_storage_key.zip'
chars = string.ascii_lowercase + string.digits
max_length = 6
found = False
password_queue = queue.Queue()

# 암호를 시도하는 함수
def worker():
    global found
    while not found:
        try:
            password = password_queue.get_nowait()
        except queue.Empty:
            return

        try:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(pwd=bytes(password, 'utf-8'))
                found = True
                print(f"\n✅ 비밀번호 해제 성공! → {password}")
                with open("password.txt", "w", encoding="utf-8") as f:
                    f.write(password)
        except:
            pass

        password_queue.task_done()

def unlock_zip_threading(thread_count=8):
    start_time = time.time()
    print("🚀 멀티스레딩으로 암호 해제 시도 중...")

    # 비밀번호 후보 큐에 저장
    for pwd_tuple in product(chars, repeat=max_length):
        password_queue.put(''.join(pwd_tuple))

    # 스레드 실행
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # 모든 작업이 끝날 때까지 대기
    password_queue.join()

    elapsed = round(time.time() - start_time, 2)
    print(f"\n⏱️ 총 소요 시간: {elapsed}초")

if __name__ == '__main__':
    unlock_zip_threading(thread_count=8)  # 스레드 개수는 시스템 성능에 맞게 조절