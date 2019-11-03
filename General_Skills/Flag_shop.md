# Flag Shop

Q) There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc 2019shell1.picoctf.com 3967.

A) picoCTF{m0n3y_bag5_cd0ead78}

Commentary:

When we net cat into the server, we are greeted with 3 choices.
1) Check Account Balance
2) Buy Flags
3) Exit

The Check Account Balance tells us that we have 1100 to use.
When trying to but flags, we get two choices.
1) Defintely not the flag Flag (Costs 900 each)
2) 1337 Flag (Costs 100.000)


Since the pricedifference between our Balance and the cost of the suspected Flag (1337 Flag),
I suspected that we could use a simple overflow attack by buying a lot of cheaper flags.
```
These knockoff Flags cost 900 each, enter desired quantity
100000000000000

The final cost is: -305594368

Your current balance after transaction: 305595468
```

This is because the system tries to do the following:
```
1100 - -305594368 
```
Which results in the large positive number.

Now we got enough funds to buy the 137 flag, which indeed holds the flag.

