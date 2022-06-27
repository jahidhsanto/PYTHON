# https://www.codechef.com/submit/CABS
for t in range(int(input())):
    X, Y, M = map(int, input().split())
    if X < Y:
        print("FIRST")
    elif X > Y:
        print("SECOND")
    else:
        print("ANY")