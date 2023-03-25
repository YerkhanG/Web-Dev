
A = set(map(int, input().split()))

n = int(input())
result = True
for i in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B) or A == B:
        result = False
        break
print(result)