There are plenty of bits of randomness in the key. This has to be secure!

I am so confident, that I am sharing a snippet of my implementation
<code>
import random
base = random.getrandbits(2048)
p = next_prime(base + random.getrandbits(256))
q = next_prime(base + random.getrandbits(256))
n = p * q
e = 65537
print("e = ", e)
print("n = ", n)
c = power_mod(m, e, n)
print("c = ", c)
</code>

########################################################


https://github.com/JimChr-R4GN4R/picoCTF-writeups/blob/master/2019/Cryptography/b00tl3gRSA3%20(450%20points)/c-n-e_-phi_-d-_plaintext.py

Flag: CTFlearn{n0t_th4t_s3cur3_4ft3r_4ll}
