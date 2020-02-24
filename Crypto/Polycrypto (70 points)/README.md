Polynomials are a very useful branch of mathematics. 

They can also hide secrets. Can you find what this one is hiding? 

https://mega.nz/#!mLJXWCIS!ZLpbPEGzhPevFeLGwUv6imuRTl19jiO5q-P7_dVaXoM 

https://en.wikipedia.org/wiki/Finite_field_arithmetic

field.txt:

<code>f = x^206 + x^205 + x^202 + x^201 + x^198 + x^197 + x^195 + x^194 + x^190 + x^189 + x^184 + x^182 + x^181 + x^178 + x^177 + x^176 + x^174 + x^173 + x^172 + x^171 + x^169 + x^168 + x^166 + x^165 + x^164 + x^157 + x^156 + x^150 + x^149 + x^147 + x^146 + x^142 + x^141 + x^140 + x^139 + x^136 + x^134 + x^133 + x^131 + x^130 + x^129 + x^126 + x^125 + x^123 + x^122 + x^121 + x^120 + x^118 + x^117 + x^115 + x^114 + x^112 + x^109 + x^108 + x^104 + x^102 + x^101 + x^96 + x^94 + x^93 + x^91 + x^90 + x^86 + x^85 + x^84 + x^81 + x^80 + x^78 + x^76 + x^75 + x^74 + x^73 + x^72 + x^69 + x^68 + x^66 + x^62 + x^61 + x^60 + x^57 + x^53 + x^52 + x^49 + x^48 + x^46 + x^44 + x^43 + x^42 + x^41 + x^40 + x^38 + x^37 + x^35 + x^33 + x^32 + x^29 + x^28 + x^21 + x^20 + x^14 + x^13 + x^11 + x^10 + x^6 + x^5 + x^4 + x^3 + x^2 + 1</code>

####################################################################################

So I visited wikipedia and I understood this:

Polynomial :  x^6 + x^4 + x + 1
Binary :        {01010011}

SO let's explain it!

We have our beginning binary number:

<code>00000000</code>

and we have this: 

<code>x^6 + x^4 + x + 1</code>

Let's take <code>x^6</code> first.

That means that we will replace the 7th from right to left (because the first zero from the right has the number place 0)

with number 1.

so our binary number will be this: <code>01000000</code>

Next we have <code>x^4</code>, so we will change the 5th zero from our binary: <code>01010000</code>

Next we have <code>x</code> this is the same like <code>x^1</code>, so : <code>01010010</code>

And finaly we will add +1 : <code>01010011</code>


So we have to do this thing with the f in field.txt

I made a python3 script for that!

Just put the f value in it and you will get the flag!

Flag: flag{p0lynom1als_4r3_k00l}
