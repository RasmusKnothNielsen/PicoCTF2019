# Unzip

Q) Can you unzip this file and get the flag?

A) picoCTF{unz1pp1ng_1s_3a5y}

Commentary:

When we unzip the zip file, we get a png file named flag.png.

Upon opening this .png, we see some text:

```
unz1pp1ng_1s_3a5y
```

When padding this with the default flag format, we get the following flag:

```
picoCTF{unz1pp1ng_1s_3a5y}
```