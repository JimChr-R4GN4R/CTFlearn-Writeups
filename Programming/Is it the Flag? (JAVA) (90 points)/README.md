Pedro was disappointed because he didn't speak Python well enough to capture some of the flags on CTFLearn. 

His plan for revenge was to create one in his native language (Java). 

The flag is a String of 6 alphanumeric characters. Capture it. 

https://mega.nz/#!SHp1xCAL!I9-Zy4kwu_JY019MiYZ6CzGey8sJ6UvqE-ML2idmkrs

#################################################################################################

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

First,we need to reach Z,so we should add +7, so the final main loop structure is:
```
for shift_0 in range(0,43):
  
  letter_0 = chr(ord(ciphertext[0]) + shift_0)
```


Flag: CTFlearn{0gHzxY}
