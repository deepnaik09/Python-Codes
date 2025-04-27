count = dict()
fname = input('Enter file name: ')
fh = open(fname)
for lines in fh:
    if lines.startswith('From '):
        words = lines.split()
        time_inp = words[5]
        time = time_inp.split(':')
        hour = time[0]
        count[hour] = count.get(hour, 0) + 1
        
lst = sorted([(key, val) for key, val in count.items()])

for key, val in lst:
    print(key, val)
        
        
        