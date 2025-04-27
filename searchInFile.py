fhand = open("mail.txt")
for line in fhand:
    line = line.strip()
    if not line.startswith("From:"):
        continue
    print(line)