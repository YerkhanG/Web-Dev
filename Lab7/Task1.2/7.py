def is_subset(A, B):
    return A.issubset(B)


T = int(input())


for t in range(T):

    n1 = int(input())
    A = set(map(int, input().split()))
    n2 = int(input())
    B = set(map(int, input().split()))
    if is_subset(A, B):
        print("True")
    else:
        print("False")