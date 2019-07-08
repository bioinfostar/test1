with open("test1.txt", "w") as fw:
    with open("test.txt", "r") as fr:
        for line in fr:
            fw.write(line)
            '''
            chr = line.split("\t")[0]
            position = line.split('\t')[1]
            '''
