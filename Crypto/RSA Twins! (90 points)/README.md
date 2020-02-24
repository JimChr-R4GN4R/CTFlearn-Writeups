https://mega.nz/#!2aBwFCKa!NWQKRIbYzSAU2iwCPNppO7SE92W6sne4FKD3sKE2A-k 

Aww, twins :). Theyâre so cute! 

They must be (almost) identical because theyâre the same except for the slightest difference. 

Anyway, see if you can find my flag. 

Hint: This is just math. You're probably not going to find any sort of specialized attack.

rsa (2).txt:

n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899

e = 65537

c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587

################################################################################

So here is clearly that we have to do with RSA.

Let's try to retrieve p from n with this https://www.alpertron.com.ar/ECM.HTM

So the p is:

<code>121588253559534573498320028934517990374721243335397811413129137253981502291629</code>

Now I used this script: https://github.com/JimChr-R4GN4R/picoCTF-writeups/blob/master/2019/Cryptography/rsa-pop-quiz%20(200%20points)/p-ct-e-n-_q-_phi-_d_pl.py

Just paste in there n,c,e and p and you will get the flag!

Flag: flag{i_l0v3_tw1N_pr1m3s}
