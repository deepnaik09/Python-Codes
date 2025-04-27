fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("File Not Found")
    quit()
count = 0
for line in fhand:
    if line.startswith("From:"):
        count += 1
print("There are", count, "From lines in", fname)
