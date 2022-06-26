# https://www.codechef.com/submit-v2/MINHEIGHT
T = int(input())
for n in range(T):
    X, H = map(int, input().split())
    if X>=H:
        print("YES")
    else:
        print("NO")