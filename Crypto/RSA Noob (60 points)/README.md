These numbers were scratched out on a prison wall.

Can you help me decode them? 

https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ

rsa.txt:

e: 1

c:9327565722767258308650643213344542404592011161659991421

n: 245841236512478852752909734912575581815967630033049838269083

#######################################################################

It's clearly RSA.

So used a script of mine that we use it when we know e,c and n

https://github.com/JimChr-R4GN4R/picoCTF-writeups/blob/master/2019/Cryptography/miniRSA%20(300%20points)/script.py

Just put in there the values and you got the flag.

Flag: abctf{b3tter_up_y0ur_e}
