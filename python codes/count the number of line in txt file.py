def count_lines(file_name):
    with open(file_name, 'r') as file:
        return sum(1 for line in file)