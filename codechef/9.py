# https://www.codechef.com/submit-v2/SUBSCRIBE_
from math import ceil

t = int(input())
for n in range(t):
    N, X = map(int, input().split())
    group = ceil(N/6)
    print(group*X)