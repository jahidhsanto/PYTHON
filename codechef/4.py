#https://www.codechef.com/submit-v2/TALLER
t = int(input())
for n in range(t):
    X, Y = map(int, input().split())
    if X > Y:
        print("A")
    else:
        print("B")