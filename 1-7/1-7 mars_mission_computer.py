import random
import datetime
import json
import time

class DummySensor:
    def __init__(self):
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
        try:
            while True:
                self.env_values = self.sensor.get_env()
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f'[{now}]')
                print(json.dumps(self.env_values, indent=4, ensure_ascii=False))
                print('-' * 40)
                time.sleep(5)  # 5초마다 반복
        except KeyboardInterrupt:
            print("\n[종료] 센서 데이터 수집을 중단했습니다.")


# 실행 부분
if __name__ == '__main__':
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()