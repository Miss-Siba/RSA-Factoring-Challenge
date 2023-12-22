#!/usr/bin/python 3
def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    signal.alarm(5)
    try:
        with open(file_path, 'r') as file:
            numbers = file.readlines()
            for number in numbers
    except (FileNotFoundError):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    for number in numbers
    if__name__ == '__main__':
        main()
