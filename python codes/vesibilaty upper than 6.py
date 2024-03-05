names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

for name in names:
    if len(name) > 6:
        print(name)