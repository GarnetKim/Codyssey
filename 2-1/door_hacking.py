import zipfile
import string
import time
from itertools import product

def unlock_zip(zip_path='emergency_storage_key.zip'):
    chars = string.ascii_lowercase + string.digits  # 소문자 + 숫자
    max_length = 6
    start_time = time.time()
    attempt_count = 0

    try:
        with zipfile.ZipFile(zip_path) as zf:
            print("🔓 비밀번호 해제 시작...")
            for password_tuple in product(chars, repeat=max_length):
                password = ''.join(password_tuple)
                attempt_count += 1

                try:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"\n✅ 비밀번호 해제 성공! → {password}")
                    elapsed = time.time() - start_time
                    print(f"🔢 총 시도 횟수: {attempt_count}")
                    print(f"⏱️ 총 소요 시간: {round(elapsed, 2)}초")

                    # 비밀번호 password.txt에 저장
                    with open("password.txt", "w", encoding="utf-8") as f:
                        f.write(password)
                    return password

                except:
                    # 해제 실패 시 다음 비밀번호 시도
                    if attempt_count % 10000 == 0:
                        print(f"시도 중... {attempt_count}회")

            print("❌ 비밀번호를 찾지 못했습니다.")
            return None

    except FileNotFoundError:
        print("📁 zip 파일을 찾을 수 없습니다.")
    except zipfile.BadZipFile:
        print("⚠️ 유효하지 않은 zip 파일입니다.")
    except Exception as e:
        print(f"⚠️ 오류 발생: {e}")

# 실행
if __name__ == '__main__':
    unlock_zip()
    

# ✅ 비밀번호 해제 성공! → mars06
# 🔢 총 시도 횟수: 726411561
# ⏱️ 총 소요 시간: 52773.37초  