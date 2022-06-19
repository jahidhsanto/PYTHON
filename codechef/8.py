# https://www.codechef.com/submit-v2/WAITTIME
t = int(input())
for n in range(t):
    K, X = map(int, input().split())
    day = K*7
    print(day-X)