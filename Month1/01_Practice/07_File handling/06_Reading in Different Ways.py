file = open("demo.txt","r")

# print(file.readline())  # Reads one line
print(file.readlines()) # Reads all lines as a list
file.close()