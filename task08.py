user = int(input('num: '))
result = 0
if user > 0:
    for i in range(1,user+1):
         result += i*i
print(result)