#https://www.codechef.com/submit-v2/AGELIMIT
t = int(input())
for n in range(t):
    X, Y, A = map(int,input().split())
    if A>=X and A<Y:
        print("YES")
    else:
        print("NO")
