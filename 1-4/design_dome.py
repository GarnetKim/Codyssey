# design_dome.py

# 전역변수 선언
result = {
    '재질': '',
    '지름': 0,
    '두께': 0,
    '면적': 0.0,
    '무게': 0.0
}

# 재료 밀도 (g/cm³)
material_density = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85
}

# 지구 중력 기준 -> 화성 중력 보정 (0.38)
GRAVITY_CORRECTION = 0.38

def sphere_area(diameter, material='유리', thickness=1):
    radius_cm = (diameter * 100) / 2  # 반지름 계산 m -> cm (입력된 지름을 cm 단위로 변환하고 2로 나눠서 반지름(cm)을 구합니다.)
    area = 2 * 3.141592 * radius_cm ** 2 # 반구의 겉면적 계산 (반구의 겉면적 = 2 * π * r²), 3.141592는 파이(π)의 근삿값
    volume = area * thickness # 재료 부피 계산 (부피 cm³ = 면적 * 두께)
    density = material_density.get(material, 2.4) #밀도값 가져오기, material_density 딕셔너리에서 재료 이름에 맞는 밀도를 가져옴, 해당 재질이 없으면 기본값 2.4(유리)를 사용
    weight = volume * density * GRAVITY_CORRECTION / 1000 #무게 계산 (질량 = 부피 cm³ * 밀도 g/cm³), (무게 = 질량 * 중력 보정 / 1000), (/ 1000은 단위 변환 (g → kg))
    # 전역 변수에 결과 저장
    result['재질'] = material
    result['지름'] = diameter
    result['두께'] = thickness
    result['면적'] = round(area, 3) # 면적을 소수점 이하 3자리까지 반올림
    result['무게'] = round(weight, 3) # 무게를 소수점 이하 3자리까지 반올림

    print(f"재질 ⇒ {result['재질']}, 지름 ⇒ {result['지름']}m, 두께 ⇒ {result['두께']}cm, 면적 ⇒ {result['면적']}cm², 무게 ⇒ {result['무게']}kg")

def run_calculator():
    while True: # 사용자가 exit하거나 n을 입력하기 전까지 계속 계산을 반복
        try:
            material = input("재질을 입력하세요 (유리, 알루미늄, 탄소강): ").strip()
            if material not in material_density:
                print("올바른 재질을 입력하세요.")
                continue

            diameter_input = input("지름을 입력하세요 (m): ").strip()
            if diameter_input.lower() == 'exit': # 사용자가 'exit'를 입력하면 계산 종료 (.lower(): 문자열을 모두 소문자로 바꾸는 메서드)
                print("계산을 종료합니다.")
                break
            diameter = float(diameter_input)
            if diameter <= 0:
                print("지름은 0보다 커야 합니다.")
                continue

            thickness_input = input("두께를 입력하세요 (기본값 1cm): ").strip()
            if thickness_input == '':
                thickness = 1
            else:
                thickness = float(thickness_input)
                if thickness <= 0:
                    print("두께는 0보다 커야 합니다.")
                    continue

            sphere_area(diameter, material, thickness)

            again = input("계속 계산하시겠습니까? (y/n): ").strip().lower()
            if again != 'y':
                print("계산을 종료합니다.")
                break

        except ValueError:
            print("숫자를 입력해야 합니다. 다시 시도해주세요.") # 예외 처리: 숫자가 아닌 값을 입력했을 때

run_calculator()
