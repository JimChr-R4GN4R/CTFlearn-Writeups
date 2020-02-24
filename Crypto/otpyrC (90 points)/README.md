Okay, this one is pretty easy... but not necessarily. 

d733432373937303734373666343730373937323733343b7644534

####################################################

Well this is HEX,so tried it by using this https://www.boxentriq.com/code-breaking/hex-analysis , but I got bad results....

Then tried to check the description a bit closer...

Then checked the title. <code>otpyrC</code>

Hmmmmm.... This is <code>Crypto</code> reversed...

Let's try decode the cipher reversed.

So I analyzed this :

<code>4354467b343337323739373037343666373437303739373234337d</code>

And I got this:

<code>CTF{43727970746f7470797243}</code>

But this flag didn't work, so tried to analyze the inside hex code <code>43727970746f7470797243</code>

and got this:

<code>CryptotpyrC</code>

Flag: CTF{CryptotpyrC}
