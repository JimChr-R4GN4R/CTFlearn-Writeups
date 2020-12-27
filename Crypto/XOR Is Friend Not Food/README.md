Here: \t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e

I think the flag started with: ctflearn{

##############################################


This is a classical XOR challenge.

We have our encrypted flag: `\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e`

and a clue: `ctflearn{`

Let's convert it to hex:
```
enc = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'hex()
091b1100160b1d19170b051d280500351b1f092c0d00181c0e
```

Now let's convert our clue to hex:
```
clue = b'ctflearn{'.hex()
6374666c6561726e7b
```

So let's try XORing the first 9 bytes with `ctflearn{` .

```

```
