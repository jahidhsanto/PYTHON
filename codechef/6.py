# https://www.codechef.com/submit-v2/BURGERS
t = int(input())
for n in range(t):
    A, B = map(int, input().split())
    if A == B:
        print(A)
    elif A > B:
        print(B)
    else:
        print(A)
