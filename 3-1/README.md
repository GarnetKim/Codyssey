# mas_map.py 코드 설명 및 수행 결과 요약

## 📌 개요
이 프로그램은 Mars 탐사 데이터(`area_map.csv`, `area_struct.csv`, `struct_category.csv`)를 활용하여 다음과 같은 분석을 수행합니다:
- 각 지역(area)별 시설 수 확인
- 시설 이름과 지형 정보 병합
- `area 1` 지역의 상세 정보 추출

## 🧾 사용된 코드

```python
import pandas as pd

def main():
    # 파일 경로
    area_map_path = "/Users/hailey/Desktop/개발/Codyssey/3-1/area_map.csv"
    area_struct_path = "/Users/hailey/Desktop/개발/Codyssey/3-1/area_struct.csv"
    struct_category_path = "/Users/hailey/Desktop/개발/Codyssey/3-1/struct_category.csv"

    # CSV 파일 읽기
    area_map_df = pd.read_csv(area_map_path)
    area_struct_df = pd.read_csv(area_struct_path)
    struct_category_df = pd.read_csv(struct_category_path)

    # 시설 종류 이름으로 병합
    merged_struct_df = area_struct_df.merge(struct_category_df, on='category', how='left')

    # 전체 지도 정보와 병합
    merged_all_df = merged_struct_df.merge(area_map_df, on=['x', 'y'], how='left')

    # 전체 area별 구조물 개수 확인
    print("🔹 시설 개수 (area별):")
    print(area_struct_df['area'].value_counts().sort_index())

    # 병합된 전체 정보 출력 (일부)
    print("\n🔹 병합된 전체 지도 정보 (상위 5개):")
    print(merged_all_df.head())

    # area 1에 해당하는 데이터만 필터링
    area_1_df = merged_all_df[merged_all_df['area'] == 1]

    # area 1 정보 출력
    print("\n🔹 Area 1에 해당하는 정보:")
    print(area_1_df.head())

if __name__ == "__main__":
    main()
```

## ✅ 수행 요약

- `area_struct.csv`의 시설 데이터를 기준으로 지역별 시설 분포를 확인.
- `struct_category.csv`와 병합하여 시설 코드를 사람이 읽을 수 있는 이름으로 변환.
- 병합된 구조물 데이터를 `area_map.csv`와 다시 병합하여 지형 정보(`mountain`) 포함된 종합 지도 생성.
- `area == 1`인 지역의 데이터만 필터링하여 탐사 거점 후보로 삼음.

## 📁 파일

- `mas_map.py`: 메인 분석 스크립트 파일
- `area_map.csv`, `area_struct.csv`, `struct_category.csv`: 입력용 데이터 파일

---
