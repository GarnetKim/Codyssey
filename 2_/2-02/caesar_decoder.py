def caesar_cipher_decode(target_text, shift): #target_text: 복호화할 문자열, shift: 얼마나 뒤로 이동시킬지 결정하는 숫자 (0~25)
    result = '' #결과를 담을 빈 문자열 생성
    for char in target_text:
        if char.isalpha(): #현재 문자가 알파벳인지 확인 (숫자나 특수문자는 그대로 둠)
            base = ord('a') if char.islower() else ord('A')
            # ord()는 문자를 아스키코드 숫자로 바꿔줘서, base는 소문자 'a' 또는 대문자 'A'의 아스키코드 값을 저장
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char #알파벳이 아니면 그대로 추가
    return result


def read_password_file(): #password_2.txt 파일을 열어 내용을 읽고 양쪽 공백 제거 후 반환
    try:
        with open("password_2.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print("❌ 'password_2.txt' 파일을 찾을 수 없습니다.")
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


def main(): #암호문 읽기 시도 후 없으면 종료
    encrypted_text = read_password_file()
    if not encrypted_text:
        return

    print("\n🔍 Caesar 암호 해독 결과 (0~25 자리수 shift):\n")
    for shift in range(26):
        decoded = caesar_cipher_decode(encrypted_text, shift)
        print(f"[{shift}] {decoded}")

    try: #사용자가 눈으로 해독 가능한 shift 번호를 직접 입력
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