file = open("demo.txt","r")

for line in file:
    print(line.strip())

file.close()