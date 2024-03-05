def count_words(file_name):
    with open(file_name, 'r') as file:
        return sum(len(line.split()) for line in file)