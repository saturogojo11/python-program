s = "Hello, World!"
for c in s:
    if c > max(s, default=c):
        print(c)
        break