import random
import datetime
import json
import time
import os
import platform

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
        ds = DummySensor()
        try:
            while True:
                ds.set_env()
                self.env_values = ds.get_env()
                print(json.dumps(self.env_values, indent=2, ensure_ascii=False)) #indent=2는 출력 시 가독성을 높이기 위해 들여쓰기를 적용, ensure_ascii=False는 한글이 깨지지 않도록 설정
                time.sleep(5)  # sleep()함수란 time 모듈 안에 있는 코드 실행을 잠시 멈추는 함수. 5초마다 반복출력
        except KeyboardInterrupt:
            print("\n[종료] 센서 데이터 수집을 중단했습니다.")

    def get_mission_computer_info(self):
        info = {
            '운영체계': platform.system(),
            '운영체계 버전': platform.version(),
            'CPU 타입': platform.processor(),
            'CPU 코어 수': os.cpu_count(),
            '메모리 크기': self._get_memory_info()
        }
        print(json.dumps(info, indent=4, ensure_ascii=False))
        return info

    def get_mission_computer_load(self):
        try:
            load_avg = os.getloadavg()
            load = {
                'CPU 실시간 사용량 (1분 평균)': load_avg[0],
                'CPU 실시간 사용량 (5분 평균)': load_avg[1],
                'CPU 실시간 사용량 (15분 평균)': load_avg[2]
            }
        except (AttributeError, OSError):
            load = {'메시지': '이 운영체제에서는 로드 평균을 지원하지 않습니다.'}

        print(json.dumps(load, indent=4, ensure_ascii=False))
        return load

    def _get_memory_info(self):
        if platform.system() == 'Darwin':
            try:
                mem_bytes = int(os.popen("sysctl -n hw.memsize").read())
                mem_gb = round(mem_bytes / (1024 ** 3), 2)
                return f"{mem_gb} GB"
            except Exception:
                return "알 수 없음"
        else:
            return "알 수 없음"

# 실행 부분
if __name__ == '__main__':
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
    runComputer.get_sensor_data()