try:
    with open("mission_computer_main.log", "r", encoding="UTF8") as f:
     lines = f.readlines()
     for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("The file 'mission_computer_main.log' does not exist.")
except PermissionError:
    print("Permission denied when trying to read 'mission_computer_main.log'.")
except UnicodeDecodeError:
    print("There was an error decoding the file 'mission_computer_main.log'. It may not be in UTF-8 format.")
except IsADirectoryError:
    print("Expected a file but found a directory instead.")
except Exception as e:
    print(f"An error occurred: {e}")
