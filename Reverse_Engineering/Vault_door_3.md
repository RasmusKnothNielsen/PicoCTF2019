# Vault door 3

Q) This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java

A) picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c08866}

Commentary:

By using the following code, we can generate the flag:

```
        String input = "jU5t_a_sna_3lpm16g84c_u_4_m0r846";

        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = input.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = input.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = input.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = input.charAt(i);
        }

        String passwd = new String(buffer);

        System.out.println("Flag:");

        System.out.println("picoCTF{" + passwd + "}");
```

This prints out:

```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c08866}
```