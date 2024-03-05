def find_words(j, k, s):
    words = s.split()
    result = []
    for word in words:
        if len(word) > j and len(word) < k:
            result.append(word)
    return result

s = "The quick brown fox jumps over the lazy dog"
j = 3
k = 6

print(find_words(j, k, s))