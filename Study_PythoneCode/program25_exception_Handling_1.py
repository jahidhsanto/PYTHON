# Exception is a runtime error
List = [20, 0, 30]
try:
    result = List[0] / List[3]
    print(result)
    print("DONE")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index error")
finally:    # Either exception handling works or not finally block must work
    print("Successfully")
