# https://www.codechef.com/submit/SIXFRIENDS
for t in range(int(input())):
    X, Y = map(int, input().split())
    if X*3>Y*2:
        print(Y*2)
    else:
        print(X*3)
