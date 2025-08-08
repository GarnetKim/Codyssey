# Mission Computer Monitoring System

## 프로젝트 개요

화성 기지에서 생존을 위한 환경 모니터링 시스템 구현 프로젝트입니다. 더미 센서를 통해 수집된 데이터를 기반으로 시스템 정보를 출력하고, 멀티프로세싱을 통해 다양한 정보를 동시에 수집합니다.

## 기능 구성

- `DummySensor` 클래스:
  - 내부/외부 온도, 습도, 광량, 이산화탄소, 산소 농도 등을 무작위 값으로 생성
  - `set_env()`로 환경값 설정, `get_env()`로 반환

- `MissionComputer` 클래스:
  - `get_sensor_data()`: 5초마다 센서 데이터 수집
  - `get_mission_computer_info()`: 20초마다 시스템 정보 출력
  - `get_mission_computer_load()`: 20초마다 CPU, 메모리 부하 출력

## 실행 방법

```bash
python mars_mission_computer.py
```

## 멀티프로세싱 구조

- 3개의 `MissionComputer` 인스턴스를 만들어 각각 다음 작업을 병렬 실행:
  - 시스템 정보 수집
  - 시스템 부하 수집
  - 센서 데이터 수집

## 제약 사항

- 기본 파이썬 모듈만 사용 가능
- 시스템 정보 수집은 `psutil`, `platform`, `os` 모듈 사용 허용
- 예외처리 필수
- 경고 메시지 없이 안정적으로 실행되어야 함
