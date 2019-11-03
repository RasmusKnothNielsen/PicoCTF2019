# 1_wanna_b3_a_r0ck5tar

Q) I wrote you another song. Put the flag in the picoCTF{} flag format

A) picoCTF{BONJOVI}

Commentary:

This one seems to be a continuation of the Mus1c challenge. 
This time it does not seem to be enough to use the online interpreter (https://codewithrockstar.com/online) 
since it only results in a pop up, that I can not provide the right answer for, if such exists.
Therefor i try to find a transpiler from rockstar to python, so it would be easier and faster
for me to understand what is going on.

I found the following github page and installed it:
https://github.com/yanorestes/rockstar-py

Converted the lyrics into a python file which can be seen in the rockstar.py file.

After this I tried to get it to run by deleting lines that did not contribute with anything 
and refactored some of the other lines, which can be seen in the fixed_rockstar.py file.

This prints out the following:
```
66
79
78
74
79
86
73
```

Put it into a decimal to ASCII converter and this is returned:
```
BONJOVI
```

And thus, our flag has been retrieved:
```
picoCTF{BONJOVI}
```