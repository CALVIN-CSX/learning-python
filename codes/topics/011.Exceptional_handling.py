# exception = An event that interrupts the flow of a program
#                     (ZeroDivisionError, TypeError, ValueError)
#                     1.try, 2.except, 3.finally
try:
    num=int(input("Enter a number: "))
    print(1/num)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You must enter a number")
except Exception:
    print("Something went wrong")
finally:
    print("do some cleanup")
