Seq1 = "ATGTTATAG"
d1 = {}
d1 = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
l = [d1[i] for i in Seq1]
result_seq = ''.join(l)
print result_seq
