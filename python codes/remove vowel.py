def remove_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join(c for c in s if c.lower() not in vowels)

s = "Hello, World!"
print(remove_vowels(s))