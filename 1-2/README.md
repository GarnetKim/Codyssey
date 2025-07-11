# 1-2-codyssey

# 🛰️ mission_computer_main 로그 분석기

이 프로젝트는 `mission_computer_main.log` 파일을 분석하여 로그를 정렬, 저장하고, 특정 문자열을 검색할 수 있는 Python 프로그램입니다.

---

## 📂 기능 요약

- 로그 파일(`.log`)을 읽어 Python 리스트 객체로 변환
- 날짜를 기준으로 시간 **역순 정렬**
- 리스트를 **사전(Dict) 객체 리스트**로 변환
- JSON(JavaScript Object Notation) 형식으로 `.json` 파일로 저장
- 특정 문자열을 포함한 로그만 **검색** 및 출력

---

## 📁 파일 구조

```
├── mission_computer_main.log        # 분석 대상 로그 파일
├── mission_computer_main.json       # 정렬 및 변환된 로그 (JSON 포맷)
├── analyzer.py                      # 메인 Python 코드
└── README.md                        # 이 문서
```

---

## 🛠️ 사용 방법

1. `mission_computer_main.log` 파일을 같은 폴더에 준비합니다.
2. `analyzer.py` 또는 main 파일을 실행합니다.

```bash
python analyzer.py
```

3. 실행 결과:
   - 로그 리스트 출력
   - `mission_computer_main.json` 파일 생성
   - 검색어 입력 시 해당 로그만 출력

---

## 🔍 예시

```
검색할 문자열을 입력하세요: Oxygen
검색 결과:
{'timestamp': '2023-08-27 11:35:00', 'event': 'INFO', 'message': 'Oxygen tank unstable.'}
{'timestamp': '2023-08-27 11:40:00', 'event': 'INFO', 'message': 'Oxygen tank explosion.'}
```

---

## 📌 주의사항

- 로그 파일은 `UTF-8` 인코딩이어야 합니다.
- 로그는 `timestamp,event,message` 형식의 CSV 구조를 따라야 합니다.
- 날짜 형식은 ISO 8601 (`YYYY-MM-DD HH:MM:SS`)여야 정렬이 올바르게 작동합니다.



