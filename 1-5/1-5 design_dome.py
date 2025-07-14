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

arr1 = np.loadtxt('mars_base_main_parts-001.csv', delimiter=',', skiprows=1)
arr2 = np.loadtxt('mars_base_main_parts-002.csv', delimiter=',', skiprows=1)
arr3 = np.loadtxt('mars_base_main_parts-003.csv', delimiter=',', skiprows=1)

"""
np.loadtxt()는 CSV처럼 숫자로만 된 파일을 빠르게 불러올 수 있는 함수
delimiter=','는 쉼표(,)로 데이터를 구분한다는 뜻
이렇게 불러오면 각 CSV 파일의 데이터가 ndarray 형식으로 저장됨

파일에 헤더(첫 줄)이 있는 경우엔 skiprows=1 옵션을 넣어야 함
- skiprows=0이면 → 'PartID', 'Strength'라는 문자열도 읽게 되므로 숫자형 데이터로 처리할 수 없어 오류 발생
- skiprows=1이면 → 숫자 데이터만 정확히 불러올 수 있음
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

