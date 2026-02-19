num = int(input())
n = len(str(num))
total = 1
count = 0
for i in range(1, n + 1):
    digit = num // 10 ** (n - i) % 10
    if digit % 2 == 0:

        print(total,'-я четная цифра равна', ' ',digit, sep='')
        total += 1
        count += 1

if count == 0:
     print('Четных цифр в числе нет')
