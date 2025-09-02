user_start = int(input('num start: '))
user_end = int(input('num end: '))

if user_start < user_end:
    for i in range(user_start,user_end + 1):
        print(i)
else:
    for i in range( user_start , user_end-1 , -1 ):
        print(i)