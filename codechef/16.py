# https://www.codechef.com/submit/FOOTCUP
for t in range(int(input())):
    X, Y = map(int, input().split())
    if X == Y and X != 0 and Y != 0:
        print("YES")
    else:
        print("NO")