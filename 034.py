l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
l.sort()
print "The smallest value in the list is: %d" % (l[0])
print "The largest value in the list is : %d" % (l[8])
dic = {}
dic[0] = l.count(0)
dic[1] = l.count(1)
dic[2] = l.count(2)
dic[3] = l.count(3)
print dic
