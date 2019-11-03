# First Grep: Part II

Q) Can you find the flag in /problems/first-grep--part-ii_4_ca16fbcd16c92f0cb1e376a6c188d58f/files on the shell server? Remember to use grep.

A) picoCTF{grep_r_to_find_this_0e28f3ee}

Commentary:

Since we are going to work on multiple files in multiple subfolders, the recursive function i grep is going to be handy.
First go to:
```
cd /problems/first-grep--part-ii_4_ca16fbcd16c92f0cb1e376a6c188d58f/
```
Then use grep with a recursive flag on files
```
grep -r pico files
```

This provides us with the flag, which were in file5 in folder files6:
