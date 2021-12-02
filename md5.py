# md5
import re 
import hashlib
filename= input("Enter Your File Name ")
f = open(filename,"r") 
data = f.read()
data2 = re.split("\s",data)
for x in data2:
    result = hashlib.md5(x.encode())
    
    print(result.hexdigest())
