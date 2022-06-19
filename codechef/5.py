# https://www.codechef.com/submit-v2/MY1STCONTEST
A, N, B = map(int, input().split())
saw = A-N
attempt = saw - B
print(saw, attempt)