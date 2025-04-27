counts = dict()
lst = list()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)

#this one line is same as the above commented code
lst = sorted([(val, key) for key, val in counts.items()], reverse=True)

for val, key in lst[:10]:
    print(key, val)
