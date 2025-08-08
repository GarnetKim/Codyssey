# 🪐 Mars Mission Computer - DummySensor

화성 기지 생존 프로젝트의 일환으로 더미 센서를 통해 내부/외부 환경 값을 시뮬레이션하는 시스템입니다.  
실제 센서를 만들기 전 테스트용으로 활용되며, 로그 기록 기능도 포함되어 있습니다.

---

## 📦 파일 구성

| 파일명 | 설명 |
|--------|------|
| `mars_mission_computer.py` | DummySensor 클래스 정의 및 센서 데이터 시뮬레이션 실행 |
| `mission_env_log.txt` | 센서 환경 데이터 로그 (자동 생성) |

---

## ⚙️ 기능

### `DummySensor` 클래스
- `env_values` (딕셔너리): 화성 기지의 내부/외부 환경 요소를 저장
- `set_env()` : 범위 내 랜덤 값을 생성하여 `env_values`에 저장
- `get_env()` : 현재 값을 반환하고 로그 파일(`mission_env_log.txt`)에 기록

### 센서 항목 및 값 범위

| 센서 항목 | 범위 |
|-----------|------|
| mars_base_internal_temperature | 18 ~ 30°C |
| mars_base_external_temperature | 0 ~ 21°C |
| mars_base_internal_humidity | 50 ~ 60% |
| mars_base_external_illuminance | 500 ~ 715 W/m² |
| mars_base_internal_co2 | 0.02 ~ 0.1% |
| mars_base_internal_oxygen | 4 ~ 7% |

---

## 🚀 실행 방법

```bash
python3 mars_mission_computer.py
```

실행 시:
1. `DummySensor` 인스턴스를 생성하고
2. `set_env()` 호출로 데이터 설정
3. `get_env()` 호출로 출력 및 로그 기록

---

## 📝 로그 파일 예시 (`mission_env_log.txt`)

```
2025-07-15 16:23:41, 24.56°C, 10.87°C, 55.12%, 684.3W/m2, 0.0342%, 5.83%
```

---

## 📌 개발 가이드

- Python 3.x 사용
- 외부 패키지 사용 불가 (`random`은 허용)
- 들여쓰기 및 변수명은 PEP8 스타일 가이드 준수

---

## ✅ 보너스 과제 포함

- `get_env()` 호출 시 로그를 `mission_env_log.txt`에 자동 기록
- 시간 정보 포함 (YYYY-MM-DD HH:MM:SS)

---

## 🙋‍♀️ 작성자

혜림 김  
부스트캠프 웹·모바일 7기 참가자  
