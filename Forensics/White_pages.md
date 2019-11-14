# White pages

Q) I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

A) picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}

Commentary:

By looking at the downloaded txt file, we can see that it definitely contains something.
When we look closer, we can see that it has two different characters.
When trying to mark one character and change all similar to either 0 or 1, 
approximately half of the characters becomes the chosen bit.
Now we try to mark one of the characters thats still "blank" and giving it the other value (0 or 1).
Now we can see that everything in the file is either 0 or 1.

When we try to convert it from binary to ASCII, we either see something intangible or we get the following:

```
picoCTF

SEE PUBLIC RECORDS & BACKGROUND REPORT
5000 Forbes Ave, Pittsburgh, PA 15213
picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}
```

And there is the flag!