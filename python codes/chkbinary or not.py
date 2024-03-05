def is_binary(input_string):
    for c in input_string:
        if c not in '01':
            return False
    return True

input_string = "10101010101"
print(is_binary(input_string))