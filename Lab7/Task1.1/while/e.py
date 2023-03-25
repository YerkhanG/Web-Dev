n = int(input())
i =0
while i < n:
    if 2**i >= n:
        print(i)
        exit()
    i+=1
