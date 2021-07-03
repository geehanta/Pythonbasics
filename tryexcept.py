


try:
    number = int(input("Enter a number: "))
    value = 10/0
    print(number)
except ZeroDivisionError:
    print("Division by zero!!")
except ValueError:
    print("Invalid input")
