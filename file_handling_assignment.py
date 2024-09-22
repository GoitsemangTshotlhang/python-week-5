# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is the first line.\n")
            file.write("This is the second line with a number: 42.\n")
            file.write("This is the third line with a string: 'Hello, World!'.\n")
        print("File created successfully!")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is the fourth line.\n")
            file.write("This is the fifth line with a number: 100.\n")
            file.write("This is the sixth line with a string: 'Goodbye, World!'.\n")
        print("File updated successfully!")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()