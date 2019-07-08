try:
    num = int(input("Enter: "))
    print(10 / num)
except ZeroDivisionError:
    print("num cannot be 0")
except ValueError:
    print("input must be exist")
