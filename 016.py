f = open('test.txt', 'r')
line = f.readlines()
for s in line:
    print(s)
f.close()
