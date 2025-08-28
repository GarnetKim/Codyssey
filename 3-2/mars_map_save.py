import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_mars_map():
    # 파일 경로
    area_map_path = "/Users/hailey/Desktop/개발/Codyssey/3-1/area_map.csv"
    area_struct_path = "/Users/hailey/Desktop/개발/Codyssey/3-1/area_struct.csv"
    struct_category_path = "/Users/hailey/Desktop/개발/Codyssey/3-1/struct_category.csv"

    # CSV 파일 읽기
    area_map_df = pd.read_csv(area_map_path)
    area_struct_df = pd.read_csv(area_struct_path)
    struct_category_df = pd.read_csv(struct_category_path)

    # struct 이름 병합
    area_struct_df = area_struct_df.merge(struct_category_df, on='category', how='left')

    # 전체 지도 병합
    merged_df = pd.merge(area_map_df, area_struct_df, how='left', on=['x', 'y'])

    # 시각화 설정
    max_x = merged_df['x'].max()
    max_y = merged_df['y'].max()

    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, max_x + 1)
    ax.set_ylim(0, max_y + 1)
    ax.set_xticks(range(1, max_x + 1))
    ax.set_yticks(range(1, max_y + 1))
    ax.grid(True)

    # 좌표를 (1,1)이 좌측상단이 되도록 반전
    ax.invert_yaxis()

    for _, row in merged_df.iterrows():
        x, y = row['x'], row['y']
        is_mountain = row['mountain']
        struct_name = row['struct']

        if is_mountain == 1:
            circle = patches.Circle((x, y), 0.45, color='saddlebrown')
            ax.add_patch(circle)
        elif struct_name == 'U.S. Mars Base Camp' or struct_name == 'Korea Mars Base':
            triangle = patches.RegularPolygon((x, y), numVertices=3, radius=0.4, orientation=0, color='green')
            ax.add_patch(triangle)
        elif pd.notnull(struct_name):
            square = patches.Rectangle((x - 0.3, y - 0.3), 0.6, 0.6, color='gray')
            ax.add_patch(square)

    ax.set_title('Mars Exploration Base Map', fontsize=15)
    plt.savefig("mars_map.png")
    plt.close()

if __name__ == "__main__":
    draw_mars_map()