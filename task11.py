num = int(input('1 - son: '))
mn = num
mx = num
for i in range(2,8):
    num = int(input(f'{i} - son: '))
    if num < mn:
        mn = num
    if num > mx:
        mx = num
print((mx + mn) / 2)