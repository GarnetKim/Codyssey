import zipfile
import string
import time
from itertools import product
from multiprocessing import Pool, cpu_count

zip_path = 'emergency_storage_key.zip'
chars = string.ascii_lowercase + string.digits
max_length = 6

def try_password(password):
    try:
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(pwd=bytes(password, 'utf-8'))
            print(f"\n✅ 비밀번호 해제 성공! → {password}")
            with open("password.txt", "w", encoding="utf-8") as f:
                f.write(password)
            return password
    except:
        return None

def unlock_zip_fast():
    start_time = time.time()
    print("🚀 병렬처리로 암호 해제 시도 중...")

    # 패스워드 후보 생성기
    all_passwords = (''.join(p) for p in product(chars, repeat=max_length))

    with Pool(processes=cpu_count()) as pool:
        for i, result in enumerate(pool.imap_unordered(try_password, all_passwords), 1):
            if i % 10000 == 0:
                print(f"시도 중... {i}회")

            if result:
                elapsed = time.time() - start_time
                print(f"🔢 총 시도 횟수: {i}")
                print(f"⏱️ 총 소요 시간: {round(elapsed, 2)}초")
                pool.terminate()
                break

if __name__ == '__main__':
    unlock_zip_fast()