s = "Hello, World!"
for c in s:
    if len(c) % 2 == 0:
        print(f"{c}: {ord(c)}")