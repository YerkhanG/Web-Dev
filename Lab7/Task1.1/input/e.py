r = 109
v = int(input())
t = int(input())
x = v*t
pos = x % 109
if pos < 0:
    pos +=109
print(pos)
