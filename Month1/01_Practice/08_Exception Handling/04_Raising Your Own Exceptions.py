age = int(input("enter your age: "))

if age < 1:

    raise ValueError("age cannot be negative or Zero")

else:
    print("valid age")


# Custom Exception Classes

class NagativeAgeError(Exception):
    pass

try:
    age = int(input("enter your age: "))

    if age < 1:

        raise NagativeAgeError("age cannot be negative or Zero")

    print("valid age")

except NagativeAgeError as e:
    print("Custom Error:", e)
