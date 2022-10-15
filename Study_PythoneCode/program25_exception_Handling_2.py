try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 / num2
    print(result)

# multiple exception in 1line
except(ValueError, ZeroDivisionError, IndexError, TabError):
    print("you have entered incorrect input.")
finally:
    print("Thanks!!!")
