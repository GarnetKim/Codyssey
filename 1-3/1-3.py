# Mars_Base_Inventory_List.csv 파일을 읽어 들여서 출력한다.
# 내용을 리스트(List) 객체로 변환한다.
# 적재 화물 목록을 인화성이 높은 순으로 정렬한다.
# 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다.
# 인화성 지수가 0.7 이상되는 목록을 Mars_Base_Inventory_danger.csv로 저장한다.

csv_filename = 'Mars_Base_Inventory_List.csv'  # 입력 파일 이름 설정
danger_filename = 'Mars_Base_Inventory_danger.csv'  # 출력 파일 이름 설정 (위험 물질 목록)

inventory_list = []  # 전체 화물 목록을 저장할 리스트
header = []  # CSV 파일의 첫 줄 (열 제목)을 저장할 리스트

# 파일을 열고 데이터를 읽어오기
try:
    with open(csv_filename, 'r', encoding = 'UTF8') as f:
        lines = f.readlines()  # 전체 줄을 리스트로 읽기
        
        for i, line in enumerate(lines):  # 한 줄씩 반복하며 줄 번호(i)도 함께 가져옴
            line = line.strip()  # 줄 앞뒤 공백 및 줄바꿈 문자 제거
            
            if not line:
                continue  # 빈 줄이면 건너뛰기
            
            parts = line.split(',')  # 쉼표 기준으로 분리 (['이름', '수량', '인화성'])
            
            if i == 0:
                header = parts  # 첫 번째 줄이면 헤더로 저장
            else:
                inventory_list.append(parts)  # 나머지 줄은 데이터로 저장

    # CSV 파일 전체 출력 (헤더 + 본문)
    print('CSV 파일 내용:')
    for row in [header] + inventory_list:
        print(row)

except FileNotFoundError:
    print(csv_filename + ' 파일이 존재하지 않습니다.')
    exit(1) # 파일이 없으면 프로그램 종료

except UnicodeDecodeError:
    print(csv_filename + ' 파일을 읽는 중에 인코딩 오류가 발생했습니다.')
    exit(1) # 파일이 없으면 프로그램 종료

except Exception as e:
    print('예상치 못한 오류가 발생했습니다:', e)
    exit(1) # 파일이 없으면 프로그램 종료

# 문자열을 실수형(float)으로 안전하게 변환하는 함수
def parse_flammability(value):
    try:
        return float(value)  # 변환 성공 시 실수 반환
    except Exception:
        return -1.0  # 변환 실패 시 기본값 -1.0 반환 (정렬 시 가장 낮음)

# 인화성 지수를 기준으로 내림차순 정렬
inventory_list.sort(key = lambda x: parse_flammability(x[-1]), reverse = True)
# x[-1]은 리스트의 마지막 항목(인화성 지수), 이를 실수로 바꿔 정렬 기준으로 사용
# reverse=True는 높은 순 → 낮은 순으로 정렬

# 인화성 지수 0.7 이상인 물질만 뽑기
danger_list = []
for row in inventory_list:
    flammability = parse_flammability(row[-1])  # 마지막 항목(인화성 지수)을 실수로 변환
    if flammability >= 0.7:
        danger_list.append(row)  # 조건에 맞는 항목만 별도로 저장

# 위험 물질 목록 출력
print('인화성 지수 0.7 이상 적재 화물 목록:')
for row in danger_list:
    print(row)

# 위험 물질 목록을 CSV 파일로 저장
try:
    with open(danger_filename, 'w', encoding = 'UTF8') as f:
        f.write(','.join(header) + '\n')  # 헤더 쓰기
        for row in danger_list:
            f.write(','.join(row) + '\n')  # 각 항목을 쉼표로 이어서 쓰기

    print(danger_filename + ' 파일이 성공적으로 생성되었습니다.')

except Exception as e:
    print(danger_filename + ' 파일 저장 중 오류가 발생했습니다:', e)