fname = input("Enter a file name: ")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        n = line.find(".")
        total += float(line[n-1:])
print("Average spam confidence: ", (total/count))