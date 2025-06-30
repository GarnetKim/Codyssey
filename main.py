try:
    with open("mission_computer_main.log", "r", encoding="UTF8") as f:
     lines = f.readlines()
     for line in lines:
            print(line.strip())
         
    # 시간 역순으로 정렬
    lines.reverse()  # Reverse the order of lines
    for line in lines:
            print(line.strip())

except FileNotFoundError: #파일이 존재하지 않을 때
    print("The file 'mission_computer_main.log' does not exist.")
except PermissionError: #파일 읽기 권한이 없을 때
    print("Permission denied when trying to read 'mission_computer_main.log'.")
except UnicodeDecodeError: #인코딩 오류 (ex.UTF-8로 못 읽을 때)
    print("There was an error decoding the file 'mission_computer_main.log'. It may not be in UTF-8 format.")
except IsADirectoryError: #파일이 아니라 디렉터리일 때
    print("Expected a file but found a directory instead.")
except Exception as e:#기타 예상 못한 모든 오류
    print(f"An error occurred: {e}")
