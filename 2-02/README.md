
# 🏛️ Caesar Cipher Decoder - 로마식 암호 해독 미션

## 📖 프로젝트 설명

화성 기지에서 추출한 `password_2.txt` 파일의 내용이 Caesar Cipher로 암호화되어 있었습니다.  
이 프로젝트는 **고대 로마의 카이사르 암호 기법**을 활용하여 해당 암호를 해독하고, 최종 결과를 `result.txt`에 저장합니다.

---

## 📝 기능 요약

- `caesar_cipher_decode()` 함수
  - 알파벳 문자만 Caesar 방식으로 `shift`만큼 뒤로 이동시켜 해독
  - 대소문자 모두 처리 가능

- `read_password_file()`
  - 암호화된 텍스트(`password_2.txt`) 읽기
  - 예외 상황에 대한 처리 포함

- `save_result_to_file()`
  - 해독이 완료된 결과를 `result.txt`로 저장

- `main()`
  - 0부터 25까지 모든 shift 값으로 복호화 시도 결과 출력
  - 사람이 직접 눈으로 읽어보고 가장 자연스러운 문장을 선택해 입력
  - 선택된 결과만 `result.txt`에 저장

---

## 📂 파일 구성

```
caesar_decoder/
│
├── caesar_decoder.py     # 본 프로그램
├── password_2.txt        # 암호화된 입력 파일 (ZIP 해제 후 생성됨)
└── result.txt            # 최종 해독 결과 저장 파일
```

---

## ⚙️ 실행 방법

```bash
python caesar_decoder.py
```

실행 시 26가지 shift에 따른 해독 결과가 모두 출력되며,  
눈으로 문장이 보이면 해당 shift 번호를 입력하여 결과를 저장합니다.

---

## 💡 제약 사항

- 외부 패키지 사용 금지 (`itertools`, `string`, `os` 등의 표준 라이브러리만 사용 가능)
- 파일 입출력 시 반드시 예외 처리가 되어 있어야 함
- 경고 없이 모든 코드가 정상적으로 실행되어야 함
- 사용자 입력을 통해 최종 복호화 값을 확인 및 저장해야 함

---

## 🧠 참고 사항

- Caesar 암호는 각 알파벳을 일정한 자리수만큼 밀어서 암호화하는 고전 암호입니다.
- 해독 시 모든 shift 조합을 시도한 후 사람이 문맥적으로 옳은 문장을 선택합니다.
- 예: `Khoor` → shift 3 → `Hello`
