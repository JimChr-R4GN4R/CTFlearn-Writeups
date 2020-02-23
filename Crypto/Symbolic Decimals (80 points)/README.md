Did you know that you can hide messages with symbols? For example, 

<code>!@#$%^&*(</code> is <code>123456789!</code>

Now Try: <code>^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%</code>

However, this isn't as easy as you might think.

###############################################

After some minutes I realised that this text is numbers when you type them with shift.

shift + 1 = !

shift + 2 = @

etc..

So I made a quick script to replace symbols with their numbers.

So let's execute it!

<code>python3 symbol_to_number.py</code>

We take this:

<code>67,84,70,123,83,116,97,114,95,46,95,87,97,114,115,95,46,95,70,111,114,95,46,95,76,105,102,101,125</code>

This is decimal so replace commas with space

<code>67 84 70 123 83 116 97 114 95 46 95 87 97 114 115 95 46 95 70 111 114 95 46 95 76 105 102 101 125</code>

and then bdecrypt it with this: https://cryptii.com/pipes/decimal-text

Flag: CTF{Star_._Wars_._For_._Life}
