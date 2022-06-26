# https://www.codechef.com/submit/FBC
for t in range(int(input())):
    K, X = map(int, input().split())
    if K-X >= 0:
        print(K-X)
    else:
        print("OVERFLOW")
