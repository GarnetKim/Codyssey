# 문제1. 미션 컴퓨터를 복구하고 사고 원인을 파악해 보자 (main.py)
# 🚀 로그 분석 보고서: mission_computer_main.log

## 📌 분석 목적
- 로켓 임무 수행 중 기록된 시스템 로그(`mission_computer_main.log`)를 분석하여 전체 진행 상황과 사고 발생 원인을 파악하고 대응 방향을 제시함.

---

## 🕒 주요 로그 요약

| 시간 | 이벤트 | 메시지 |
|------|--------|--------|
| 10:00 | INFO | Rocket initialization process started. |
| 10:30 | INFO | Liftoff! Rocket has left the launchpad. |
| 10:45 | INFO | Second stage ignition. Rocket continues its ascent. |
| 11:05 | INFO | Satellite deployment successful. Mission objectives achieved. |
| 11:28 | INFO | Touchdown confirmed. Rocket safely landed. |
| 11:35 | INFO | **Oxygen tank unstable.** |
| 11:40 | INFO | **Oxygen tank explosion.** |
| 12:00 | INFO | Center and mission control systems powered down. |

---

## 🔍 이상 징후 및 사고 분석

### 1. **정상 작동**
- 10:00부터 11:30까지 로켓 발사, 궤도 진입, 위성 배치, 귀환까지 모든 단계가 정상적으로 진행됨.
- 로그 상 모든 시스템 상태는 `INFO` 수준으로 기록됨.

### 2. **사고 발생**
- 11:35: **산소탱크 불안정(Oxygen tank unstable)** 로그 기록
- 11:40: **산소탱크 폭발(Oxygen tank explosion)** 로그 기록
- 12:00: **센터 및 미션 제어 시스템 종료(Powered down)** 기록

### 🚨 분석
- **폭발 이전 경고 없이 INFO 수준으로 기록되어 있음** → 로그 레벨 관리 필요
- 폭발 원인은 `산소탱크 불안정`으로 추정되며, 빠르게 폭발로 이어진 것으로 보임
- 폭발 후 로그 기록이 존재하는 것으로 보아, 폭발이 로켓 자체가 아닌 지상 또는 분리된 모듈에서 발생했을 가능성 있음

---

## ✅ 결론 및 제안

### 📌 결론
- 로켓 임무는 **성공적으로 수행되었으나**, **귀환 후 산소탱크 폭발 사고 발생**
- 미션 본체에는 치명적 영향이 없었던 것으로 보이며, 로그 시스템은 정상 작동

### 💡 제안
- **산소탱크 상태에 대한 센서 감시 강화**
- 로그 레벨 설정 개선: 위험 징후는 `WARNING` 또는 `CRITICAL`로 기록 필요
- 폭발 원인에 대한 별도 하드웨어 진단 필요
- 향후 로그에 **비정상 상태를 자동 탐지하는 분석 시스템** 연동 제안

---

## 📁 파일 정보

- 로그 파일: `mission_computer_main.log`
- 분석 일시: 2025-06-30
- 담당자: 김혜림
- 분석 도구: Python (`main.py`)
