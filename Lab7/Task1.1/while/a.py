import math
n = int(input())
i =1
while i!=n+1:
    if(i % math.sqrt(i) == 0):
        print(i)
    i+=1