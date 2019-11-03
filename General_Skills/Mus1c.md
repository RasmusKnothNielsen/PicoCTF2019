# Mus1c

Q) I wrote you a song. Put it in the picoCTF{} flag format

A) picoCTF{rrrocknrn0113r}

Commentary:

No apparent clues are left in the .txt file and no usable meta data is available.
The hint says something about rockstar
```
Do you think you can master rockstar?
```
After some thought, I remember reading something about a programming language called Rockstar, 
which use song texts as input.

I found a webpage that could execute Rockstar code and pasted the lyrics into it.
https://codewithrockstar.com/online

This was the output:
```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```

I tried converting it from binary to ASCII and got the following:
```
rrrocknrn0113r
```

This is indeed the flag: 
```
picoCTF{rrrocknrn0113r}
```