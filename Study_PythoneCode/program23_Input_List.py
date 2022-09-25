n = input("Enter a text of number: ")
list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)
print(sum)

numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text: ")
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numOfLetters += 1
    elif x >= '0' and x <= '9':
        numOfDigits += 1
    elif x == ' ':
        numOfWords += 1
print("Number of letters: ", numOfLetters)
print("Number of digits: ", numOfDigits)
print("Number of words: ", numOfWords + 1)
