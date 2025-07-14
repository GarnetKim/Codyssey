# 🚀 Mars Base Structural Analysis with NumPy

화성 기지의 구조 강도 분석을 위한 NumPy 기반 데이터 처리 프로젝트입니다.  
세 개의 부품 목록 CSV 파일을 통합하여 평균값을 계산하고, 기준 이하의 데이터를 선별하여 보강 대상으로 저장합니다.

---

## 📁 프로젝트 개요

### 🎯 수행 목표
- `mars_base_main_parts-001.csv`, `002.csv`, `003.csv` 파일을 numpy로 읽기
- 3개의 배열을 병합하여 `parts` 배열 생성
- 각 부품 수치의 평균을 계산
- 평균값이 `50 미만`인 부품 목록을 `parts_to_work_on.csv`에 저장
- 전치행렬 계산 (보너스)

---

## 📌 주요 기능

- `np.genfromtxt()`를 이용한 CSV 파일 읽기
- `np.concatenate()`를 이용한 배열 병합
- `np.mean()`을 사용한 평균 계산
- 마스킹 조건으로 평균 이하 값 필터링
- 전치행렬 계산 및 저장 (보너스)

---

## 🧪 실행 방법

1. Python 3.x와 numpy가 설치되어 있어야 합니다.

```bash
pip install numpy
```

2. `design_dome.py` 파일을 실행합니다.

```bash
python3 design_dome.py
```

3. 결과:
   - 평균값 출력
   - 평균 미만 부품 목록 출력
   - `parts_to_work_on.csv` 파일 생성
   - 전치행렬 출력 (보너스)

---

## 📂 출력 예시

```txt
전체 부품 수치의 평균값: 52.471
평균값이 50보다 작은 부품 목록:
['A010' 42]
['A015' 36]
...

'parts_to_work_on.csv' 파일이 성공적으로 저장되었습니다.

전치행렬 (parts3):
[['42' '36' ...]]
```

---

## 🛠️ 예외 처리

- 파일 경로 오류, 저장 실패 등의 예외 상황에 대한 try-except 처리
- 사용자에게 오류 메시지를 명확히 출력

---

## 🎁 보너스 과제

- `parts_to_work_on.csv` → `parts2` 배열로 로드
- `parts2`에서 숫자 데이터 추출 → 전치행렬 생성
- `parts3`로 저장 및 출력

---

## 🧠 학습 포인트

- numpy 배열 구조와 연산 이해
- 문자열+숫자 혼합 CSV 데이터 처리
- 평균 및 조건 필터링 처리
- 전치행렬(Transpose)의 개념과 사용법

---

## 📄 파일 구성

| 파일명 | 설명 |
|--------|------|
| `design_dome.py` | 메인 분석 코드 |
| `mars_base_main_parts-001.csv` | 부품 목록 파일 1 |
| `mars_base_main_parts-002.csv` | 부품 목록 파일 2 |
| `mars_base_main_parts-003.csv` | 부품 목록 파일 3 |
| `parts_to_work_on.csv` | 평균 이하 부품 목록 저장 파일 |

---

## 🙋‍♀️ 사용 조건

- 외부 라이브러리 금지 (단, `numpy` 사용 가능)
- 모든 코드 Python 3.x 기반 작성
- 파일 저장 시 반드시 예외 처리 포함

---

