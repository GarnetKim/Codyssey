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
