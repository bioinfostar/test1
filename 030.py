Seq1 = "AGTTTATAG"

import re 
p = re.compile('TT')
result = p.finditer(Seq1)
for r in result:
    print r.start()
