# 🔥 Mars Base Inventory Analyzer

화성 기지의 적재 화물 목록을 분석하여 **인화성이 높은 위험 물질**을 식별하고, 이를 **별도 파일로 저장**하는 Python 스크립트입니다.

---

## 📁 프로젝트 구성

| 파일명 | 설명 |
|--------|------|
| `Mars_Base_Inventory_List.csv` | 원본 화물 목록 CSV 파일 |
| `Mars_Base_Inventory_danger.csv` | 인화성 지수 0.7 이상인 위험 화물 목록 (자동 생성) |
| `inventory_analyzer.py` | 데이터 분석 파이썬 스크립트 |
| `README.md` | 프로젝트 설명서 |

---

## 🚀 실행 방법

### 1. Python 버전 확인
# Mars Base Inventory Processor

## Project Overview
이 프로젝트는 화성 기지 입고 물질 목록(`Mars_Base_Inventory_List.csv`)을 읽어 인화성 지수를 기준으로 정렬하고, 위험 물질(인화성 지수 0.7 이상)을 별도로 분류하여 CSV 파일로 저장하는 기능을 제공합니다.

## Features
- CSV 파일을 리스트(List) 객체로 변환
- 인화성 지수 기준 내림차순 정렬
- 위험 물질(인화성 지수 ≥ 0.7) 자동 분류
- 위험 물질 목록을 별도 CSV 파일로 저장
- 파일 처리 시 예외 처리

## Requirements
- Python 3.x
- 별도의 외부 라이브러리 불필요 (표준 라이브러리만 사용)

## Usage
1. `Mars_Base_Inventory_List.csv` 파일을 현재 디렉토리에 준비합니다.
2. 아래 명령어로 프로그램을 실행합니다:
   ```bash
   python 1-3.py
   ```
3. CSV 파일 내용이 출력되고, 인화성 지수 기준으로 정렬됩니다.
4. 인화성 지수 0.7 이상인 위험 물질 목록이 출력됩니다.
5. 위험 물질 목록이 `Mars_Base_Inventory_danger.csv` 파일로 저장됩니다.

## Input Format
```
Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
Alcohol,0.789,0.79,Very weak,0.85
Petroleum Products,Various,Various,Various,0.92
...
```

## Output Format
### Console Output
- 원본 CSV 파일 내용
- 인화성 지수 0.7 이상인 위험 물질 목록

### Generated File: Mars_Base_Inventory_danger.csv
```
Substance,Weight (g/cm³),Specific Gravity,Strength,Flammability
Gunpowder,Various,Various,Various,0.98
Hydrogen Peroxide,1.45,1.45,Very low,0.98
...
```

## File Structure
```
project/
├── 1-3 main.py                      # 메인 실행 파일
├── Mars_Base_Inventory_List.csv     # 입력 데이터 파일
├── Mars_Base_Inventory_danger.csv   # 생성되는 위험 물질 목록
└── README.md                        # 프로젝트 문서
```

## Error Handling
- 파일이 존재하지 않는 경우
- 파일 인코딩 오류
- 파일 읽기/쓰기 권한 오류
- 기타 예상치 못한 오류

## License
[MIT License](LICENSE) 또는 조직/개인에 맞는 라이선스를 명시하세요. 
Python 3.x 이상이 설치되어 있어야 합니다.

```bash
python --version
