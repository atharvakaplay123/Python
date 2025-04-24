#for detailed description about exception handling in python, visit: https://www.geeksforgeeks.org/python-exception-handling/
from time import sleep   
print("This is a simple command line calculator made using exception handling in python\nThankyou for using it\n")
while True:
    try: #it is the code where the error can happen
        print("Answer: ", eval(input(">> ")))
        sleep(0.01)

    except KeyboardInterrupt: #it will run when the specified error happens
        print("Exited By the User")
        sleep(2)
        break

    except ZeroDivisionError: #it will run when the specified error happens
        print("Can't be divided by zero!")

    except NameError: #it will run when the specified error happens
        print("only numbers allowed\nPlease Retry")

    else: #it will run only if there is not exception
        print("calculation done") 

    finally: #it will run irrespective of the exception
        print("\nPlease enter the next exp")