# https://www.codechef.com/submit/MANIPULATE
for t in range(int(input())):
    X, Y = map(int, input().split())
    if X >= Y:
        print("YES")
    else:
        print("NO")
