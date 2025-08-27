# iPhone 스타일 공학용 계산기 UI (PyQt6)

이 프로젝트는 PyQt6를 활용하여 만든 **공학용 계산기 UI**입니다. <br>
계산 기능은 아직 구현되어 있지 않으며, 버튼을 누르면 입력란에 해당 텍스트가 출력되는 UI 프로토타입입니다.

---

## 📋 기능

- 공학용 계산기 레이아웃 구현
- 버튼 클릭 시 디스플레이에 텍스트 출력
- PyQt6 기반 사용자 인터페이스
- 둥근 모서리 스타일 버튼
- Rad, π, sin, log 등 공학 연산 버튼 포함

---

## 🧪 설치 및 실행 방법

1. Python 설치 (버전 3.7 이상 권장)
2. PyQt6 설치:
```bash
pip install PyQt6
```
3. 파일 실행:
```bash
python engineering_calculator.py
```

---

## 📁 파일 구성

| 파일명        | 설명                                      |
|---------------|-------------------------------------------|
| `engineering_calculator.py` | 메인 GUI 계산기 코드 (PyQt6 기반)         |
| `README.md`    | 프로젝트 설명 파일                         |

---

## 🛠 사용된 기술

- Python 3
- PyQt6
- QVBoxLayout, QGridLayout, QPushButton, QLineEdit

---

## ✅ TODO

- 버튼 기능에 맞는 실제 연산 로직 구현
- 메모리 관련 버튼 (mc, m+, m-, mr)
- 삼각함수 및 로그 함수 계산
- 'Rad'와 'Deg' 토글 기능
