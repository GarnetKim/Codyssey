import random
import datetime
import json
import time
import os
import platform
import psutil
import threading
import multiprocessing

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
                self.sensor.set_env()
                self.env_values = self.sensor.get_env()
                print('[센서 데이터]', json.dumps(self.env_values, indent=2, ensure_ascii=False))
                time.sleep(5)
        except KeyboardInterrupt:
            print("\n[종료] 센서 데이터 수집을 중단했습니다.")

    def get_mission_computer_info(self):
        try:
            while True:
                info = {
                    '운영체계': platform.system(),
                    '운영체계 버전': platform.version(),
                    'CPU 타입': platform.processor(),
                    'CPU 코어 수': os.cpu_count(),
                    '메모리 크기': self._get_memory_info()
                }
                print('[시스템 정보]', json.dumps(info, indent=4, ensure_ascii=False))
                time.sleep(20)
        except KeyboardInterrupt:
            print("\n[종료] 시스템 정보 수집 중단")

    def get_mission_computer_load(self):
        try:
            while True:
                load = {}
                try:
                    load_avg = os.getloadavg()
                    load['CPU 실시간 사용량 (1분 평균)'] = load_avg[0]
                except Exception:
                    load['CPU 부하'] = '로드 평균을 가져올 수 없습니다.'
                try:
                    memory = psutil.virtual_memory()
                    load['메모리 실시간 사용량'] = f"{memory.percent}%"
                except Exception:
                    load['메모리 실시간 사용량'] = '알 수 없음'
                print('[시스템 부하]', json.dumps(load, indent=4, ensure_ascii=False))
                time.sleep(20)
        except KeyboardInterrupt:
            print("\n[종료] 시스템 부하 수집을 중단했습니다.")

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

# 스레드로 실행
def run_with_threads():
    computer = MissionComputer()
    threading.Thread(target=computer.get_mission_computer_info).start()
    threading.Thread(target=computer.get_mission_computer_load).start()
    threading.Thread(target=computer.get_sensor_data).start()


# 멀티프로세스로 실행
def run_with_processes():
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info)
    p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load)
    p3 = multiprocessing.Process(target=runComputer3.get_sensor_data)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
    # 스레드 실행
    # run_with_threads()

    # 프로세스 실행
    run_with_processes()
