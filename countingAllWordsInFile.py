list1 = []
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    x = line.rstrip()
    words = x.split()
    for word in words:
        if word not in list1:
            list1.append(word)
list1.sort()
print(list1)