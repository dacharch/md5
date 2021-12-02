# md5
import re 
import hashlib
import sys
filename= sys.argv
f = open(filename[1],"r") 
data = f.read()
data2 = re.split("\s",data)
for x in data2:
    result = hashlib.md5(x.encode())
    
    print(result.hexdigest())
