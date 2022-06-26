# https://www.codechef.com/submit/WATERCOOLER1
for t in range(int(input())):
    X, Y, M = map(int, input().split())
    if X*M < Y:
        print("YES")
    else:
        print("NO")
