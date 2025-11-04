try:

    num = int(input("enter num"))
    print(10/num)


    # Handling Specific Exceptions

except ZeroDivisionError:
    print("You can’t divide by zero!")

except ValueError:
    print("Please enter a valid number.")

except:

    print("something went to wrong")
