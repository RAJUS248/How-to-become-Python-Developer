# else Block

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero not allowed.")
else:
    print("Division successful!")  # runs only if no error


# finally Block

try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")

