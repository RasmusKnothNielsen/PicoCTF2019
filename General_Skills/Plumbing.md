# Plumbing

Q) Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 21550.

A) picoCTF{digital_plumb3r_8f946c69}

Commentary:

Since we want to keep whatever comes from our netcat connection, we want to echo it into a file locally.
```
nc 2019shell1.picoctf.com 21550 > result.txt
```

Now we can easily grep this file to find the flag

```
grep pico result.txt
```