Can you help me? 

I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. 

Please! Here is the file: https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys

############################################################################################################################

So let's begin!

We have the data.dat file which contains many lines with 1s and 0s (you can check it in this folder).

So let's understand what he wants...

Let's say we have this line: 
`0001100000101010100`

Let's translate it into programming language!

I will use python3.

So first we need to read our file!

```
file_text = open('data.dat') # open file
file_text = file_text.read() # read it's content
```
Done!

Now if you have some experience with python3 you should know that when we read a file,for some (unkown to me) reason, it reads one extra empty line at the end...

So just add this command:
`file_text = file_text[:-1]`

We are done with the file import part.

Let's move to our loop!

So we have to make a loop that reads each line at every repeat.

So we will split our `file_text` at every line change.

`file_text = file_text.split('\n')`

and next we will put a counter:
`counter = 0`

So now we will make our loop!

```
for current_line in file_text: # current_line = '0001100000101010100' , then the next line...

    zeros_number = current_line.count('0') # Current line's 0s /// Here are 13
    ones_number = current_line.count('1') # Current line's 1s /// Here are 6
```

So now let's return to the description!

He tells us this:
`number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2`

That means our counter will rise by +1 when one of these situations is True.

So let's make our if!

number of 0's is a multiple of 3:
`zeros_number % 3 == 0`

Because:

1 % 3 = 1 # False

7 % 3 = 1 # False

3 % 3 = 0 # True

9 % 3 = 0 # True

First if is done!

Let's move to the second one:
`ones_number % 2 == 0`

Because:

1 % 2 = 1 # False

7 % 2 = 1 # False

2 % 2 = 0 # True

8 % 2 = 0 # True

So now we should merge them with OR.

So this is our final if:
```
for current_line in file_text:

    zeros_number = current_line.count('0') # Current line's 0s
    ones_number = current_line.count('1') # Current line's 1s
    
    
    if (zeros_number % 3 == 0) or (ones_number % 2 == 0):
        counter += 1 # counter = counter + 1
```

and finally when the loop will end we will print counter's value:
`print(counter)`

And run it!
`python3 script.py`

You can check the final script in `script.py` file.

Flag: CTFlearn{6662}
