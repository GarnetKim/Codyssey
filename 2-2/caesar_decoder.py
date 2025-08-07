def caesar_cipher_decode(target_text, shift):
    result = ''
    for char in target_text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            # 알파벳을 shift만큼 뒤로 이동
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


def read_password_file():
    try:
        with open("password 2.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("❌ 'password 2.txt' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"❌ 파일을 읽는 중 오류 발생: {e}")
    return None


def save_result_to_file(result):
    try:
        with open("result.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("✅ 결과가 result.txt 파일에 저장되었습니다.")
    except Exception as e:
        print(f"❌ 결과 저장 중 오류 발생: {e}")


def main():
    encrypted_text = read_password_file()
    if not encrypted_text:
        return

    print("\n🔍 Caesar 암호 해독 결과 (0~25 자리수 shift):\n")
    for shift in range(26):
        decoded = caesar_cipher_decode(encrypted_text, shift)
        print(f"[{shift}] {decoded}")

    try:
        selected = int(input("\n👀 복호화된 문장이 보이면 해당 shift 번호를 입력하세요: "))
        if 0 <= selected < 26:
            result = caesar_cipher_decode(encrypted_text, selected)
            save_result_to_file(result)
        else:
            print("❌ 0에서 25 사이의 숫자만 입력하세요.")
    except ValueError:
        print("❌ 유효한 숫자를 입력해주세요.")


if __name__ == "__main__":
    main()