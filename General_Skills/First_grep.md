# First Grep
Q) Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_4_6b0be85ad029e98c683231bdafec396c on the shell server.

A) picoCTF{grep_is_good_to_find_things_ad4e9645}

Commentary:

I like to traverse to the destination folder, to take a look at what's going on.
Do this by going up 2 folders and enter the folder from the question.
```
cd ../../problems/first-grep_4_6b0be85ad029e98c683231bdafec396c
```
Here we see a file named file, which is a ASCII text file. It's easy to perform a grep on it, to reveal the flag:
```
grep pico file
```
Which indeed provides the flag = picoCTF{grep_is_good_to_find_things_ad4e9645}