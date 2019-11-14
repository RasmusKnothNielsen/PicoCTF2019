# Extensions

Q) This is a really weird text file TXT? Can you find the flag?

A) picoCTF{now_you_know_about_extensions}

Commentary:

After downloading the weird .txt file, i run a file command on it:

```
file flag.txt
```

This returns:

```
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

So now I change the extension to .png instead and lo and behold, here is the flag:

```
picoCTF{now_you_know_about_extensions}
```