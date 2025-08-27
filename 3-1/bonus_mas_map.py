import pandas as pd

# 📂 CSV 파일 불러오기
area_map = pd.read_csv('/Users/hailey/Desktop/개발/Codyssey/3-1/area_map.csv')
area_struct = pd.read_csv('/Users/hailey/Desktop/개발/Codyssey/3-1/area_struct.csv')
struct_category = pd.read_csv('/Users/hailey/Desktop/개발/Codyssey/3-1/struct_category.csv')

# 🧹 열 이름 공백 제거 (혹시 모를 에러 방지)
struct_category.columns = struct_category.columns.str.strip()
area_struct.columns = area_struct.columns.str.strip()

# 🔗 시설 데이터와 카테고리 병합 (category 기준)
area_struct = area_struct.merge(struct_category, how='left', on='category')

# 🗺️ 지도 데이터와 병합
full_map = area_map.merge(area_struct, on=['x', 'y'], how='left')

# 📊 시설 개수 요약
facility_summary = full_map['struct'].value_counts(dropna=False).rename_axis('시설 종류').reset_index(name='개수')

# 🏔️ 산악 지형 유무 요약
mountain_summary = full_map['mountain'].value_counts().rename_axis('산악 지형 여부').reset_index(name='칸 수')
mountain_summary['산악 지형 여부'] = mountain_summary['산악 지형 여부'].map({0: '평지', 1: '산악지형'})

# 🗺️ 지역별 시설 수 요약
area_facility_summary = full_map.groupby('area')['struct'].count().rename('시설 수').reset_index()

# 🖨️ 결과 출력
print('\n🔸 시설 종류별 개수:')
print(facility_summary)

print('\n🔸 산악 지형 분포:')
print(mountain_summary)

print('\n🔸 지역(area)별 시설 수:')
print(area_facility_summary)