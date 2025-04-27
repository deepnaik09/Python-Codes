file_name = input("Enter file name: ")
try:
    fhand = open(file_name+".txt", 'r')
    print("File opened")
except FileNotFoundError:
    print("File not found")


