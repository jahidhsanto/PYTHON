# https://www.codechef.com/submit-v2/CHAIRS_
t = int(input())
for n in range(t):
    X, Y = map(int, input().split())
    Z = X-Y
    if Z<=0:
        print("0")
    else:
        print(X-Y)