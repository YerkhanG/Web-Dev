import numpy

arr = []
for _ in range(int(input())):
    arr.append(list(map(float,input().split())))
out = numpy.linalg.det(numpy.array(arr))
#print("{0:.2f}".format(out))
print(round(out,2))
