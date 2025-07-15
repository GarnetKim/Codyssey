import random
import datetime

class DummySensor:
    def __init__(self): #__init__()는 클래스가 초기화될 때 자동으로 실행되는 생성자 메소드, self는 앞으로 생성될 인스턴스
        self.env_values = { # env_values는 DummySensor 클래스의 멤버 변수(속성)
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }

    def set_env(self): # set_env()는 DummySensor 클래스의 메소드로, 환경 변수를 무작위로 설정
         self.env_values['mars_base_internal_temperature'] = random.uniform(18, 30)
         self.env_values['mars_base_external_temperature'] = random.uniform(0, 21)
         self.env_values['mars_base_internal_humidity'] = random.uniform(50, 60)
         self.env_values['mars_base_external_illuminance'] = random.uniform(500, 715)
         self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
         self.env_values['mars_base_internal_oxygen'] = random.uniform(4, 7)

    def get_env(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_line = (
            f'{now}, '
            f"{self.env_values['mars_base_internal_temperature']}°C, "
            f"{self.env_values['mars_base_external_temperature']}°C, "
            f"{self.env_values['mars_base_internal_humidity']}%, "
            f"{self.env_values['mars_base_external_illuminance']}W/m2, "
            f"{self.env_values['mars_base_internal_co2']}%, "
            f"{self.env_values['mars_base_internal_oxygen']}%\n"
        )
        try:
            with open('mission_env_log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(log_line)
        except Exception as e:
            print('로그 파일 저장 중 오류:', e)

        return self.env_values

# 인스턴스 생성 및 테스트 실행
ds = DummySensor()
ds.set_env()
env = ds.get_env()

# 결과 출력
print('현재 센서 데이터:')
for key, value in env.items():
    print(f'{key} : {value}')