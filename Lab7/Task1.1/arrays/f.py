n = int(input())
a=list(map(int, input().strip().split()))
cnt = 0
for i in range(1,n-1):
    if (a[i] > a[i-1] and a[i] > a[i+1]):
        cnt+=1
print(cnt)