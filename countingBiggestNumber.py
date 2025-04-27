counts = dict()
fname = input("Enter file name: ")
fh = open(fname)
for lines in fh:
    if lines.startswith('From '):
        words = lines.split()
        word = words[1]
        counts[word] = counts.get(word, 0) + 1
bigword = None
bigcount = None
for key, value in counts.items():
    if bigcount == None or value > bigcount:
        bigword = key
        bigcount = value
print(bigword, bigcount)