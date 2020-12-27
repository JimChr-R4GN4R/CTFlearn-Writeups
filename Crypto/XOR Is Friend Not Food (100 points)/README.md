Here: \t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e

I think the flag started with: ctflearn{

##############################################


This is a classical XOR challenge.

We have our encrypted flag: `\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e`

and a clue: `ctflearn{`


Let's convert it to hex:
```
enc = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'hex()
enc = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'.hex()
091b1100160b1d19170b051d280500351b1f092c0d00181c0e
091b1100160b1d19170b051d280500351b1f092c0d00181c0e
```


So let's try to XOR the first 9 bytes with our clue:
```
from Crypto.Util.number import long_to_bytes
int( enc[:len(clue)] , 16 ) ^ int( clue ,16 )
long_to_bytes(1963386879516613769068)
b'jowlsjowl'
```

We get the result `jowlsjowl`!


Our encrypted flag has totaly 25 bytes, so our key is `jowlsjowlsjowlsjowlsjowls`.
Let's try to XOR them:
```
key = b'jowlsjowlsjowlsjowlsjowls'.hex()
flag = long_to_bytes( int((enc.hex()),16) ^ int(key,16))
```

Flag: ctflearn{xor_is_the_goop}
