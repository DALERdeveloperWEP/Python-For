user = int( input("num: ") )

if user <= 15:
    for i in range(user,16):
        print(i)
else:
    for i in range(user,15,-1):
        print(i)