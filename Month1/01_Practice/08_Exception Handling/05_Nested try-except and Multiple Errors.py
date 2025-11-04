try:
    x = int(input("enter number: "))
    y = int(input("enter number: "))

    print(x/y)

except(ValueError,ZeroDivisionError) as e:
    print("Error occurred:", e)