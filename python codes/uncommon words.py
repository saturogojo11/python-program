def uncommon_words(s1, s2):
    words1 = set(s1.split())
    words2 = set(s2.split())
    return words1.symmetric_difference(words2)

s1 = "GeeksforGeeks"
s2 = "Codefreaks"
print(list(uncommon_words(s1, s2)))