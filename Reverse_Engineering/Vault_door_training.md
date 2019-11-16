# Vault door training

Q) Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. 
The laboratory is protected by a series of locked vault doors. 
Each door is controlled by a computer and requires a password to open. 
Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, 
but one of our junior agents obtained the source code for each vault's computer! 
You will need to read the source code for each level to figure out what the password is for that vault door. 
As a warmup, we have created a replica vault in our training facility. 
The source code for the training vault is here: VaultDoorTraining.java

A) picoCTF{w4rm1ng_Up_w1tH_jAv4_c0b141c5e30}

Commentary:

When we open the VaultDoorTraining.java file, we find the password on line 23:

```
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_c0b141c5e30");
    }
```

Pad this with the flag format, and get the following flag:

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_c0b141c5e30}
```