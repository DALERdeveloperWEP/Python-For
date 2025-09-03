user = int(input('num: '))
juft = 0
toq = 0
for i in range(1,user + 1):
   if i % 2 == 0:juft += i 
   if i % 2 != 0:toq += i 
print(juft,toq)