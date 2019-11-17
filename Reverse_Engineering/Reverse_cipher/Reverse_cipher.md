# Reverse cipher

Q) We have recovered a binary and a text file. Can you reverse the flag. 
Its also found in /problems/reverse-cipher_4_12cef42b8e03692a36099b293f991a41 on the shell server.

A) picoCTF{r3v3rs32ccdd282}

Commentary:

This problem uses a rotation encryption on the content of the flag, so we have to find it.
The following solution provides us with the correct flag:
```
        String ciphertext = "picoCTF{w1{1wq80haib767}";
        char[] plaintext = ciphertext.toCharArray();

        for (int i = 22; i >=8; i--) {
            char newchar = ciphertext.charAt(i);

            if ((i & 1) == 0) {
                plaintext[i] = (char) (newchar - 5);
            } else {
                plaintext[i] = (char) (newchar + 2);
            }
        }

        String password = new String(plaintext);
        System.out.println(password);
```

This gives us the correct flag:

```
picoCTF{r3v3rs32ccdd282}
```
