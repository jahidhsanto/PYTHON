from collections import deque

bank = deque(["Jahid", "Foysal", "Nabila"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)

if not bank:
    print("No person left")
