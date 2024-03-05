def remove_char(s, n):
    return s[:n] + s[n+1:]
s = input("Enter a string: ")
n = int(input("Enter the index to remove: "))
print("New string:", remove_char(s, n))