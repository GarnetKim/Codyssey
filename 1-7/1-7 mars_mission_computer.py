import random
import datetime
import json
import time

class DummySensor:
    def __init__(self): #__init__()는 클래스가 초기화될 때 자동으로 실행되는 생성자 메소드, self는 앞으로 생성될 인스턴스
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        self.set_env()
        return self.env_values


class MissionComputer:
    def __init__(self):
        self.env_values = {}
        self.sensor = DummySensor()

    def get_sensor_data(self):
        ds = DummySensor()
        try:
            while True:
                ds.set_env()
                self.env_values = ds.get_env()
                print(json.dumps(self.env_values, indent=2, ensure_ascii=False)) #indent=2는 출력 시 가독성을 높이기 위해 들여쓰기를 적용, ensure_ascii=False는 한글이 깨지지 않도록 설정
                time.sleep(5)  # sleep()함수란 time 모듈 안에 있는 코드 실행을 잠시 멈추는 함수. 5초마다 반복출력
        except KeyboardInterrupt:
            print("\n[종료] 센서 데이터 수집을 중단했습니다.")


# 실행 부분
if __name__ == '__main__':
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()

