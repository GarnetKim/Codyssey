import json
# mission_computer_main.log 파일을 읽어들여서 출력한다. 콤마를 기준으로 날짜 및 시간과 로그 내용을 분류해서 Python의 리스트(List) 객체로 전환한다.
# (여기서 말하는 리스트는 배열이 아니라 파이썬에서 제공하는 리스트 타입의 객체를 의미한다.)
# 전환된 리스트 객체를 화면에 출력한다.
# 리스트 객체를 시간의 역순으로 정렬(sort)한다.
# 리스트 객체를 사전(Dict) 객체로 전환한다.
# 사전 객체로 전환된 내용을 mission_computer_main.json 파일로 저장하는데 파일 포멧은 JSON(JavaScript Ontation)으로 저장한다.

log_list = []

try:
    with open('mission_computer_main.log', 'r', encoding='UTF8') as f:
        lines = f.readlines()  # 파일의 모든 줄을 읽어들임

    # 첫 줄은 헤더이므로 제외
    data_lines = lines[1:]
    
    for line in data_lines:
        parts = line.strip().split(',', 2)  # 최대 3조각으로 자르기
        if len(parts) == 3:
            timestamp, event, message = parts
            log_list.append([timestamp, event, message])

    # 결과 출력 (전체 리스트)
    print('리스트 객체:')
    for entry in log_list:
        print(entry)

except FileNotFoundError:
    print('mission_computer_main.log 파일이 현재 디렉토리에 존재하지 않습니다.')
    exit(1)
except UnicodeDecodeError:
    print('mission_computer_main.log 파일을 읽는 중에 인코딩 오류가 발생했습니다.')
    exit(1)
except Exception as e:
    print('예상치 못한 오류가 발생했습니다:', e)
    exit(1)

# 시간의 역순으로 정렬 (문자열 기준이지만 ISO8601이므로 가능)
log_list.sort(key = lambda x: x[0], reverse = True)

# 리스트 객체를 사전(Dict) 객체의 리스트로 전환
log_dict_list = []
for log in log_list:
    log_dict = {'timestamp': log[0], 'event': log[1], 'message': log[2]}
    log_dict_list.append(log_dict)

# JSON 파일로 저장 (json 모듈 사용)
with open('mission_computer_main.json', 'w', encoding='UTF8') as json_file:
    json.dump(log_dict_list, json_file, ensure_ascii = False, indent = 4)

print('mission_computer_main.json 파일이 성공적으로 생성되었습니다.')

# 사전 객체로 전환된 내용에서 특정 문자열 (예를 들어 Oxygen)을 입력하면 해당 내용을 출력하는 코드를 추가한다.
search_str = input('검색할 문자열을 입력하세요: ')
print('검색 결과:')
for log_dict in log_dict_list:
    found = False
    for value in log_dict.values():
        if search_str in value:
            found = True
            break
    if found:
        print(log_dict)
