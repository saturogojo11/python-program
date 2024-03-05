def check_substring(input_string, substring):
    input_string = input_string.lower()
    if substring in input_string:
        return True
    else:
        return False

input_string = "secret websites"
substring = "secret"
print(check_substring(input_string, substring))