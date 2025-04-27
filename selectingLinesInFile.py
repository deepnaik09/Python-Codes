fhand = open("mail.txt")
for line in fhand:
    line = line.rstrip()
    if not 'deepnaik1809' in line:
        continue
    print(line)