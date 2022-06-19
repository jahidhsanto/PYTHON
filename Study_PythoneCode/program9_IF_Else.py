mark=int(input("Enter mark: "))
if mark>=80 and mark<=100:
    print("A+")
    print("CONGRATULATIONS")
elif mark<80 and mark>=75:
    print("A")
elif mark<75 and mark>=70:
    print("A-")
elif mark<70 and mark>=65:
    print("B+")
elif mark<65 and mark>=60:
    print("B")
elif mark<60 and mark>=55:
    print("B-")
elif mark<55 and mark>=50:
    print("C+")
elif mark<50 and mark>=45:
    print("C")
elif mark<45 and mark>=40:
    print("D")
elif mark<40 and mark>=0:
    print("FAIL")
else:
    print("!!!<TRY AGAIN>!!!")


print("Program END")