
# 📄 파일 처리 예외 설명 (Python)

파일 입출력을 다룰 때 발생할 수 있는 주요 예외를 정리한 문서입니다.

---

## ✅ 주요 예외 목록 및 설명

| 예외 이름 | 발생 조건 | 설명 및 해결 방법 |
|-----------|------------|-------------------|
| `FileNotFoundError` | 지정한 파일이 없을 때 | 경로 또는 파일명이 정확한지 확인 |
| `PermissionError` | 읽기/쓰기 권한이 없을 때 | 관리자 권한 또는 파일 접근 권한을 확인 |
| `IsADirectoryError` | 파일 대신 디렉터리를 열려고 할 때 | 경로가 파일인지 디렉터리인지 확인 |
| `UnicodeDecodeError` | 텍스트 파일의 인코딩 문제 | `encoding='utf-8'` 대신 다른 인코딩(CP949 등)을 시도 |
| `Exception` | 그 외 모든 예외 | 예상하지 못한 오류를 포착하고 디버깅하는 데 사용 |

---

## ✅ 예외 처리 예시 코드

```python
try:
    with open("파일명", "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except PermissionError:
    print("파일 접근 권한이 없습니다.")
except UnicodeDecodeError:
    print("인코딩 오류입니다.")
except IsADirectoryError:
    print("파일이 아닌 디렉터리를 열려고 했습니다.")
except Exception as e:
    print(f"기타 오류 발생: {e}")
```

---

## 📌 참고
- 항상 `try-except` 구문으로 감싸 안전한 코드 작성을 권장
- 파일을 다룰 때는 `with open(...)` 구문을 사용하면 자동으로 파일이 닫혀서 안전
