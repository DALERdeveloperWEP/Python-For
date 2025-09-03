num = int(input('1 - narx: '))
mn = num
mx = num
for i in range(2,6):
    num = int(input(f'{i} - narx: '))
    if num < mn:
        mn = num
    if num > mx:
        mx = num
print(mn,mx)