# https://www.codechef.com/submit/SNDMAX
for t in range(int(input())):
    X, Y, Z = map(int, input().split())
    if X >= Y and X >= Z:
        if Y >= Z:
            print(Y)
        else:
            print(Z)
    elif Y>=X and Y>=Z:
        if X >= Z:
            print(X)
        else:
            print(Z)
    elif X >= Y:
        print (X)
    else:
        print(Y)
