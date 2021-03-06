Pedro was disappointed because he didn't speak Python well enough to capture some of the flags on CTFLearn. 

His plan for revenge was to create one in his native language (Java). 

The flag is a String of 6 alphanumeric characters. Capture it. 

https://mega.nz/#!SHp1xCAL!I9-Zy4kwu_JY019MiYZ6CzGey8sJ6UvqE-ML2idmkrs

#############################################################################################

From description we see that the flag has total 6 alphanumeric characters.

So the downloaded file was this java script:
```
public class IsItTheFlag {

public static boolean isFlag(String str) {
	return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;
}

public static void main(String[] args) {

String flag = "------";

if (isFlag(flag))
	System.out.println("You found it!");
else
	System.out.println("Try again :(");

	}
}
```



If we read cearfully the code, we will see that there is a flag variable which theoritically has our flag.

Then he sends it to `isFlag` function via `str` variable and he does this:

`return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;`

I searched on google about `str.hashCode() java` and found this: https://www.tutorialspoint.com/java/java_string_hashcode.htm

and this: https://howtodoinjava.com/java/string/string-hashcode-method/

So we understood good enough what does this command do.

After that I searched for `Reverse String.hashCode()` but as I was expecting,I could not find something...

Then I tried to make a brute script in java but I succesfully failed :P (learned some new things though :D )

After some time of research, I decided to search for `.hashCode() python` and found this page:

http://garage.pimentech.net/libcommonPython_src_python_libcommon_javastringhashcode/

I took this function and checked if it was giving the same results as like java and it did! :
```
def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000
```

Then I started scripting `script1.py`

So let's start!

We added our `.hashCode()` function.

Then we have to make our ciphertext which will have 6 alphanumeric characters. 

I imagined it to start from `000000` to `zzzzzz`

But with this way I have to include uppercase characters...BUT if we check the java code, we will see this:

`str.toLowerCase().hashCode() == 1472541258`

That means our ciphertext.hashCode() with all it's characters to be lowcased should give `1472541258`.

So at first we do not need to include Uppercase alphabet.

Let's make our beginning ciphertext:

`ciphertext = "000000"`

Our ciphertext has all numbers ( 0-9 ) and lowercase alphabet ( a-z ).

We will split our ciphertext to 6 parts:

`ciphertext = list(ciphertext)`

ciphertext's every part has totally 10 + 26 = 36 characters (0123456789abcdefghijklmnopqrstuvwxyz)

The plan is to make loops that at every repeat,they will shift +1 every part of our ciphertext.

So I found this: https://stackoverflow.com/questions/12797067/how-can-i-do-a-1-b-in-python

From there we get this thing:

```
Our first ciphertext's character is: ciphertext[0] = "0"

chr(ord(ciphertext[0]) + 1 = "1"

If ciphertext[0] = "a"
then
chr(ord(ciphertext[0]) + 1 = "b"
```

So at the beginning I did this:
```
ciphertext = list(ciphertext)

for shift_0 in range(0,36):
  
  letter_0 = chr(ord(ciphertext[0]) + shift_0)
  print(letter_0)
```
But I was getting this:
```
0
1
2
3
4
5
6
7
8
9
:
;
<
=
>
?
@
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
```

First,we need to reach Z,so we should add +7 at 36,

and second we do not need special characters,so we will add an if down of the shift calculation.

So the final main loop structure is:
```
for shift_0 in range(0,43):
  
  letter_0 = chr(ord(ciphertext[0]) + shift_0)
  
    if chr(ord(ciphertext[0]) + 1) == ":":
    	letter_0 = "a"
```

This is our completed loop:
```
for shift_0 in range(0,43):
  
  letter_0 = chr(ord(ciphertext[0]) + shift_0)

  if chr(ord(ciphertext[0]) + 1) == ":":
    letter_0 = "a"

  for shift_1 in range(0,43):
    letter_1 = chr(ord(ciphertext[1]) + shift_1)

    if chr(ord(ciphertext[1]) + 1) == ":":
      letter_1 = "a"

    for shift_2 in range(0,43):
      letter_2 = chr(ord(ciphertext[2]) + shift_2)

      if chr(ord(ciphertext[2]) + 1) == ":":
        letter_2 = "a"

      for shift_3 in range(0,43):
        letter_3 = chr(ord(ciphertext[3]) + shift_3)

        if chr(ord(ciphertext[3]) + 1) == ":":
          letter_3 = "a"

        for shift_4 in range(0,43):
          letter_4 = chr(ord(ciphertext[4]) + shift_4)

          if chr(ord(ciphertext[4]) + 1) == ":":
            letter_4 = "a"

          for shift_5 in range(0,43):
            letter_5 = chr(ord(ciphertext[5]) + shift_5)

            if chr(ord(ciphertext[5]) + 1) == ":":
              letter_5 = "a"
```

So now we will add our `final_ciphertext` variable which will take the `letter_x` variables.

Firstly we will set this variable at the beginning of the code before loops:

`final_ciphertext = ""`

Then in the last for, we will add this:

`            final_ciphertext = letter_0+letter_1+letter_2+letter_3+letter_4+letter_5`

and finally we will add an if down of it:

```
            if int(java_string_hashcode(final_ciphertext.lower())) == 1472541258:
	    	print(final_ciphertext)
```

Here we see firstly: `final_ciphertext.lower()` which means that `final_ciphertext`'s letters will be lowercase.

Next we will send it's value to `java_string_hashcode()` function and it will return it's `.hashCode()` value.

Next with `int(...)` we will make sure that the number it will send,will be the same type as like `1472541258` which is an integer.

And hat's it!

You can find the full code in `script1.py` .

So let's run it!

`python3 script1.py`

For some reason that I cannot think right now,at some `letter_x` there will be some special characters...

But we do not care very much right now.

After 2-3 minutes, it will give us this result:
```
0GHZXY
0GHZZ;
0GJ<XY
0GJ<Z;
0GJ>:Y
0GJ><;
```
We do not care about the results with special characters,so we will choose the first one which is `0GHZXY` .

So we have our flag!

But wait... The java script also has this: `str.hashCode() == 1471587914` which the value is different of ours.

That means that some letters are in lowercase and some are in uppercase.

So let's make another bruteforce script that will test all possible lower and uppercase combinations!

First we will keep our `.hashCode()` function . so let's add it first...

```
def java_string_hashcode(s):
    h = 0
    for c in s:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000
```

Next we will add our `text` and will split it into 6 parts,

then we will set our `final_text` variable

and at last we will add our `target` value:

```
text = "0GHZXY"
target = 1471587914

final_text = ""

target = 1471587914
```

Next I decided to follow this bruteforce method:

We will have another variable called `final_bin`.

This variable at the beginning will be

final_bin = "000000"

and will be rising with binary way.

At the places where is zero,the letters will be zero and where is one, letter will be upper.

Examples:
```
final_bin = "000000"
text      = "0ghzxy"

final_bin = "000001"
text      = "0ghzxY"

final_bin = "100110"
text      = "0ghZXy"

etc.
```

We will make a for that at every repeat will add +1 into `final_bin`

`final_bin`'s minimum value is `000000 = 0` and the maximum is `111111 = 63`

That means our for will be like this:
```
for i in range(0,64): # it's until 64,because at 63 will stop
	....
	....
```

next we will add this command to give `i`'s binary value to `number`:
```
for i in range(0,64):
	number = bin(i)
```

and then we will add this command to add `number`'s value to `final_text` and make it have 6 digits:
```
final_bin = "{:06d}".format(int(number))
```
Example:
```
if number = 1
final_bin = "{:06d}".format(int(number)) = "000001"
if number = 3
final_bin = "{:06d}".format(int(number)) = "000011"
etc...
```
I found this here: https://stackoverflow.com/questions/134934/display-number-with-leading-zeros

and then we will split it's parts:
```
final_bin = list(final_bin)
```

So now we have this:
```
for i in range(0,64):
  number = bin(i)
  number = number.replace('0b','')

  final_bin = "{:06d}".format(int(number))
  final_bin = list(final_bin)
```

Now at every repeat we will make 6 ifs that check if every `final_bin`'s part is zero or one and if is 1,then same `text`'s part will be uppercase else,it will be lowercase.

So here are our ifs:
```
for i in range(0,64):

  number = bin(i)
  number = number.replace('0b','')

  final_bin = "{:06d}".format(int(number))
  
  final_bin = list(final_bin)
  
  if int(final_bin[0]) == 1:
    text[0] = text[0].lower()
  else:
    text[0] = text[0].upper()
    
  if int(final_bin[1]) == 1:
    text[1] = text[1].lower()
  else:
    text[1] = text[1].upper()
    
  if int(final_bin[2]) == 1:
    text[2] = text[2].lower()
  else:
    text[2] = text[2].upper()
    
  if int(final_bin[3]) == 1:
    text[3] = text[3].lower()
  else:
    text[3] = text[3].upper()
    
  if int(final_bin[4]) == 1:
    text[4] = text[4].lower()
  else:
    text[4] = text[4].upper()
    
  if int(final_bin[5]) == 1:
    text[5] = text[5].lower()
  else:
    text[5] = text[5].upper()
```

Now we will make `final_text` variable which will merge all text's parts that are uppercase and lowercase

Then we will send it to our `.hashCode()` function and will asign it's result to `result` variable

And lastly will add an if that checks if `result` is the same as our `target`'s value:
```
  final_text =  str(text[0]) + str(text[1]) + str(text[2]) + str(text[3]) + str(text[4]) + str(text[5])
  result = java_string_hashcode(final_text)
  
  if int(result) == target:
    print(final_text)
```

Now we are almost ready.

The only thing is that at the beginning of the loop,we change `final_bin`'s string value.But after the first repeat,it's type will change to list.

So we have to make it change it's type to string at every beginning of all repeats.

So just add this command at the beginning of the loop:
```
for i in range(0,64):
  final_bin = str(final_bin)
  ....
  ....
```
You can find the final script in `script2.py`

After we run it...
```
python3 script2.py
```

After some seconds we will take this result:
```
0gHzxY
0gHzxY
```
I do not know why it print's it two times though :P , but it works!!!

Flag: CTFlearn{0gHzxY}
