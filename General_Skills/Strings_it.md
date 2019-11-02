#Strings it
###Q) Can you find the flag in file without running it? You can also find the file in /problems/strings-it_1_7a67382a38fc00751a6b9b29b0872813 on the shell server.

###A) picoCTF{5tRIng5_1T_0690b2a5}

##Commentary:
Go to the folder in question, and find the strings file.
Perform a strings command on the strings file:
```
strings strings
```

And realise that there is a lot of strings in the file.
This is where grep becomes usable again:
```
strings strings | grep pico
```

Which reveals the flag: picoCTF{5tRIng5_1T_0690b2a5}