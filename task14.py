num = int(input('1 - yosh: '))
result = num
for i in range(2,6):
    num = int(input(f'{i} - yosh: '))
    result += num

print(result / 5)