Skynet is using a very small list of primes for RSA style encryption purposes. 

In fact their list is only the size of the smallest odd prime. 

One of the robots sent a message to three other robots. 

These are futuristic robots with the ability to use quantum computing and so they don't mind prime factoring huge numbers.

You can't do that though. Find out what message the robot sent to his friends. Flag is in flag{} format. 

https://mega.nz/#!7WZg2I5I!UiyBukv8_IjartojnY86nhN5jsQFKE4tPCEF1lPqsQ8

Skynet.txt:

```
e: 65537
c1: 5024836662627906750454817701922271080214720765897113783786369197810770999608528443597447448508876214100063962982376037712548944474807897847869334582773452689962992522987755069402952836848501053684233233850594080254869
n1: 10603199174122839808738169357706062732533966731323858892743816728206914395320609331466257631096646511986506501272036007668358071304364156150345138983648630874220488837685118753574424686204595981514561343227316297317899

c2: 130884437483098301339042672379318680582507704056215246672305503902799253294397268030727540524911640778691710963573363763216872030631281953772411963153320471648783848323158455504315739311667392161460121273259241311534
n2: 5613358668671613665566510382994441407219432062998832523305840186970780370368271618683122274081615792349154210168307159475914213081021759597948038689876676892007399580995868266543309872185843728429426430822156211839073

c3: 40136988332296795741662524458025734893351353026652568277369126873536130787573840288544348201399567767278683800132245661707440297299339161485942455489387697524794283615358478900857853907316854396647838513117062760230880
n3: 43197226819995414250880489055413585390503681019180594772781599842207471693041753129885439403306011423063922105541557658194092177558145184151460920732675652134876335722840331008185551706229533179802997366680787866083523
```

#########################################################################################

So we have `e` , some `n` and their `c` .

After some research I found that we can do 'Hastad's Broadcast Attack'

You can find a good source here about it:

https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption/Attack-Hastad-Broadcast



We can find <code>p1,p2,p3</code> with this way:

```
p1 = gcd(n1,n2)
p2 = gcd(n2,n3)
p3 = gcd(n1,n3)
```
GCD(n1,n2) is the `Greatest Common Divisor` and can be calculated with this python3 script:

```
n1_value = n1_NUMBER
n2_value = n2_NUMBER

def ComputeGCD(n1,n2):
    if n2==0:
        return n1
    else:
        return ComputeGCD(n2 , n1 % n2)

print(ComputeGCD(n1_value,n2_value))
```

So now from `n` and `p`, we can find `q` with this calculation:

`q1 = n1//p1`

The difference between `n1/p1` and `n1//p1` is this:

```
q1 = n1/p1 = 9.033062119150775e+108
q1 = n1//p1 = 9033062119150775356115605417902072538098631081058159551678022048966520848600866260935959311606867286026034943
```

So now we have `e`,`n`,`q`,`p` and `c` .

So we can find `phi = (q - 1) * (p - 1)` 

and when we find all `phi`s, then we can find `d = e^(-1) MOD phi` with this python3 script:

```
from Crypto.Util.number import inverse

e = e_NUMBER
phi = phi_NUMBER

d = inverse(e, phi)
```

So now the only we need to find to find is `plaintext` by `c`,`d` and `n` .

We can find plaintext with this simple python3 script:

```
c = c_NUMBER
d = d_NUMBER
n = n_NUMBER

plaintext = pow(c, d, n) # (ciphertext^d) MOD n
```

When we get all plaintexts,then we have to convert them from text to hex and then to ascii.

We can do it with this script:
```
pl = plaintext_NUMBER

pl_hex_converted = hex(pl).split('x')[-1] # convert plaintext to hex
pl_from_hex_to_ascii = bytearray.fromhex(pl_hex_converted).decode() # convert hex to ascii
```
So `pl_from_hex_to_ascii` is our flag!

I made a quick script that does all these steps I descripted above,so you can just type `python3 script.py`
and you will see that all plaintext variables are the same flag!

Flag: flag{will_he_be_back}
