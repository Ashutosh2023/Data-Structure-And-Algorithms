a= 6.789
num = abs(a)
counter = 0
while num != 0:
    num = num//10
    counter+=1
    if(counter>10):
        break

print(counter)
