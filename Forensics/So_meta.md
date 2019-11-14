# So meta

Q) Find the flag in this picture. You can also find the file in /problems/so-meta_6_8d7541b8d04bd65a01336fdb8db6db24.

A) picoCTF{s0_m3ta_505fdd8b}

Commentary:

When we download the picture, we take a look at it. 
This does not provide any obvious flags, so we try the next thing.

When performing a Strings on the picture, we get the flag in the last portion of the Strings.
We try to pipe it over to a grep, to see if there is anything else of interest:

```
Strings pico_img.png | grep pico
```
And here is the flag:

```
picoCTF{s0_m3ta_505fdd8b}
```