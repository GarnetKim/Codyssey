"""
<수행과제>
- numpy를 사용하기 위해서 import를 한다.
- csv 파일들을 모두 numpy를 사용해서 읽어들여서 각각 arr1, arr2, arr3 과 같이 ndarray로 저장한다.
- 3개의 배열을 하나로 합치고 이름을 parts 라는 ndarray로 저장한다.
- parts를 이용해서 각 항목의 평균값을 구한다.
- 평균값이 50보다 작은 값을 뽑아내서 parts_to_work_on.csv 파일로 저장한다.
- 작성된 코드는 design_dome.py 라는 이름으로 저장한다.
- 파일로 저장하는 부분에는 반드시 예외처리가 되어 있어야 한다.
"""

import numpy as np
arr1 = np.genfromtxt('/Users/hailey/Desktop/Codyssey/1-5/mars_base_main_parts-001.csv',
                     delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
arr2 = np.genfromtxt('/Users/hailey/Desktop/Codyssey/1-5/mars_base_main_parts-002.csv',
                     delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
arr3 = np.genfromtxt('/Users/hailey/Desktop/Codyssey/1-5/mars_base_main_parts-003.csv',
                     delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

"""
np.genfromtxt() : 텍스트 파일(CSV 포함)을 배열로 읽어옴
delimiter=',' : 쉼표 구분자 사용
skip_header=1 : 첫 줄(헤더)을 건너뜀
dtype=None : 자동으로 자료형 추론
encoding='utf-8' : UTF-8 인코딩으로 읽음
이렇게 불러오면 각 CSV 파일의 데이터가 ndarray 형식으로 저장됨

np.genfromtxt()에서 skiprows는 지원하지 않는 키워드
→ 대신 skip_header 를 사용해야 함
"""

parts = np.concatenate((arr1, arr2, arr3)) 
# concatenate는 여러 배열을 하나로 합치는 함수

"""
지금 상태의 parts 배열은 구조화 배열(structured array)이며, 다음과 같은 형태를 갖고 있음

dtype=[('f0', '<U25'), ('f1', '<i8')]
# f0: 부품 이름 (문자열)
# f1: 수치 데이터 (정수)

f1 항목만 추출해서 평균값을 계산하면 됨
"""
mean_value = np.mean(parts['f1'])

print(f'전체 부품 수치의 평균값: {mean_value:.3f}')

"""
parts['f1']: 모든 부품의 수치 데이터만 추출
np.mean(...): 평균값 계산
:.3f: 소수점 아래 3자리까지 출력
"""

# 평균값이 50보다 작은 부품들만 필터링
parts_to_work_on = parts[parts['f1'] < 50]

print('평균값이 50보다 작은 부품 목록:')
for part in parts_to_work_on:
    print(part)

"""
parts['f1'] < 50
→ f1 값이 50보다 작은 행에 대해 True/False 마스크 생성
parts[ ... ]
→ 조건에 맞는 행만 선택하여 parts_to_work_on이라는 새로운 배열 생성
"""

output_filename = 'parts_to_work_on.csv'

try:
    # 헤더 포함 저장
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('id,mean_value\n')  # 헤더 작성
        for part in parts_to_work_on:
            f.write(f'{part["f0"]},{part["f1"]}\n')
    print(f"'{output_filename}' 파일이 성공적으로 저장되었습니다.")
except Exception as e:
    print(f"파일 저장 중 오류가 발생했습니다: {e}")

"""
id와 mean_value라는 열 이름으로 헤더를 먼저 작성
parts_to_work_on 배열의 각 행에서 f0(id), f1(평균값)을 추출하여 한 줄씩 CSV로 저장
파일 저장 중 문제가 생기면 에러 메시지를 출력
"""

# 보너스 문제
# parts_to_work_on.csv 파일을 다시 읽어들여서 출력하기
# parts2의 내용을 기반으로 전치행렬을 구하고 그 내용을 parts3에 저장하고 출력한다.

import numpy as np

try:
    parts2 = np.genfromtxt('parts_to_work_on.csv', delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
    print('parts2 내용:')
    print(parts2)
except Exception as e:
    print(f"파일을 읽는 중 오류가 발생했습니다: {e}")

import numpy as np

try:
    # CSV 파일 읽기 (헤더 제외)
    parts2 = np.genfromtxt('parts_to_work_on.csv', delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
    
    # 부품 ID (문자열)와 수치 데이터 (숫자)가 섞여 있으므로 수치 데이터만 따로 추출
    numeric_values = np.array([row[1] for row in parts2])

    # 1차원 배열을 2차원 배열로 변환한 후 전치
    numeric_matrix = numeric_values.reshape(1, -1)  # shape: (1, N)
    parts3 = numeric_matrix.T  # 전치 후 shape: (N, 1)

    print('전치행렬 parts3:')
    print(parts3)

except Exception as e:
    print(f"오류 발생: {e}")

"""
row[1]: parts2에서 수치값(두 번째 열)만 추출
.reshape(1, -1): 1행 N열 형태로 재구성(-1은 열의 개수를 자동 계산하라는 의미, 즉 “1행 N열짜리 2차원 배열로 만들어줘!” 라는 뜻)
.T: 전치행렬(행 ↔ 열 뒤바꿈)
parts3: 전치된 ndarray 객체
"""

output_file = 'parts_transposed.csv'

try:
    # 파일로 저장
    np.savetxt(output_file, parts3, delimiter=',', fmt='%.3f', encoding='utf-8')
    print(f"전치행렬이 '{output_file}' 파일로 성공적으로 저장되었습니다.")
except Exception as e:
    print(f"파일 저장 중 오류가 발생했습니다: {e}")

"""
np.savetxt()는 단순한 수치 배열을 CSV 형식으로 저장할 때 유용함
fmt='%.3f'는 소수점 아래 3자리까지 저장함
encoding='utf-8'을 넣어서 한글 환경에서도 깨지지 않도록 함
parts_transposed.csv 파일이 생성됨
"""
