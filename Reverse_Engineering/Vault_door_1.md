# Vault door 1

Q) This vault uses some complicated arrays! I hope you can make sense of it, special agent. 
The source code for this vault is here: VaultDoor1.java

A) picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_2487f0}

Commentary:

When we open the source code, we can see that the array is scrambled.
One way to get the password out, without taking consideration to how long it is, is to use the find and replace method.

With this, we can find every instance of
```
.charAt(
```
And replace it with 
```
[
```

Every instance of 
```
)  =
```
And replace it with
```
]
```

And every instance of 
```
 &&
```

and replace it with
```
;
```

Thus we get the following code, that is easier to execute:
First we have to initialize an array to hold the chars, so we do that.

```
char[] password = new char[32];

        password[0] = 'd';
        password[29] = '7';
        password[0]  = 'd';
        password[29] = '7';
        password[4]  = 'r';
        ...
        System.out.println(password);
```

This provides us with the password:
```
d35cr4mbl3_tH3_cH4r4cT3r5_2487f0
```



