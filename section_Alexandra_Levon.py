name = input()
counter = 0
a = 0
while name != 'Левон':
    if name == 'Александра':
        a += 1
    elif a == 1:
        counter += 1
    name = input()
print(counter)
