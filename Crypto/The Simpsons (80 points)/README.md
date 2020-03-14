Ya know, I was thinking... wouldn't the Simpsons use octal as a base system? They have 8 fingers... 

Oh, right! The problem! Ummm, something seems odd about this image... 

https://mega.nz/#!yfp1nYrQ!LOz_eucuKkjAaDqVvz3GWgbfdKWn8BhussKZbx6bUMg

##############################################################################################

So I downloaded a .jpg file and opened terminal and typed <code>strings image_file_name.jpg</code>

At the end of the results I found this:

```
Ahh! Realistically the Simpsons would use octal instead of decimal!
encoded = 152 162 152 145 162 167 150 172 153 162 145 170 141 162
key = chr(SolutionToDis(110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051))
key = key + key + chr(ord(key)-4)
print(DecodeDat(key=key,text=encoded))
```

So from the hint from description and from the text at the first line of the above result I decided to use this http://www.unit-conversion.info/texttools/octal/#data to convert from octal to text.

so <code>152 162 152 145 162 167 150 172 153 162 145 170 141 162 = jrjerwhzkrexar</code>

`encoded = 'jrjerwhzkrexar'`

Then I did the same with the key value...

and the result was this:

`How much did Maggie originally cost? (Divided by 8, to the nearest integer, and then plus four)`

So I searched on google "How much did Maggie originally cost simpsons" and I got this:

`Maggie originally scanned for $847.63, which was the price of raising a baby for one month back in 1989 (when the show debuted). Now things have changed and Marge's groceries add up to $243.36. When Maggie is added and scanned, she doubles the tab to $486.52.`

So I took the 847.63 and followed the instructions...

`847.63 / 8 = 105.95375`

105.95375 nearest integer is 106 .

`106 + 4 = 110`

So the result is:

`key = chr(110)`


So our final script is:

```
encoded = 'jrjerwhzkrexar'
key = chr(110)
key = key + key + chr(ord(key)-4)
print(DecodeDat(key=key,text=encoded))
```

We have the last one which does not make sense cause of the strange function called 'DecodeDat'...

I tried to execute this python code but I got only an error...

Then I was curious what key's final value was...So I updated the code:

```
encoded = 'jrjerwhzkrexar'
key = chr(110)
key = key + key + chr(ord(key)-4)
print(key)
```

and got the final key: `nnj`

Then I suspected that he uses some Ciphers which needs a key like this...

So I used this: https://cryptii.com and at the beginning I chose the Vigenere Cipher.

And this was it!

just put as encrypted message the 'jrjerwhzkrexar' and as key the 'nnj' and you will get this:

`wearenumberone`

Flag: CTFlearn{wearenumberone}
