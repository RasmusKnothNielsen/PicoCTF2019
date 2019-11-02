# Whats a net cat?
###Q) Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 37851 to get the flag?

###A) picoCTF{nEtCat_Mast3ry_628e0244}

Commentary:
This is straight forward, just open another terminal and nc to the server:
```
nc 2019shell1.picoctf.com 37851
```

Which reveals the flag: picoCTF{nEtCat_Mast3ry_628e0244}