# Vault door 4

Q) This vault uses ASCII encoding for the password. The source code for this vault is here: VaultDoor4.java

A) picoCTF{jU5t_4_bUnCh_0f_bYt3s_7a1c8c668b}

Commentary:

By taking the byte array from the java file, and convert it into a new string, we can get the flag:
```
        byte[] myBytes = {
                106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
                0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
                0142, 0131, 0164, 063 , 0163, 0137, 067 , 0141,
                '1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b' ,
        };

        String password = null;
        try {
            password = new String(myBytes, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        System.out.println("picoCTF{" + password + "}");
```

This prints out the flag to the console:

```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_7a1c8c668b}
```

