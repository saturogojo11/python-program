def read_file_line_by_line(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())