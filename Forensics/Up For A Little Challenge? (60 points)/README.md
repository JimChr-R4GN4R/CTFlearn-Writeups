https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0

You Know What To Do ...

######################################################################

Okay, the file that is downloaded is called "Begin Hack.jpg"

So I executed <code>strings Begin Hack.jpg</code>

And at some point I found these that took my attention:

<code>flag{Not_So_Simple...}</code>

<code>password: Really? Again</code>

<code>Mp real_unlock_key: Nothing Is As It SeemsU</code>

<code>`- https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg</code>

which are at the end of the results.

So first I tried to download the file that new mega.nz address has.

The file that was downloaded is called "Up For A Little Challenge.zip"

Inside it, it has a folder called "Did I Forget Again?"

and inside this folder there are two files...

- .Processing.cerb4
- Loo Nothing Becomes Useless ack.jpg

After the extraction I first tried <code>strings Loo\ Nothing\ Becomes\ Useless\ ack.jpg</code>

But I did not find something interesting...

Then I tried to analyze the other file.

The first thing that came in my mind was to do <code>file .Processing.cerb4</code>

and the result was this: <code>.Processing.cerb4: Zip archive data, at least v2.0 to extract</code>

So added the extension .zip and the final name of the file is <code>.Processing.cerb4.zip</code>

and then I opened it.

Inside it it had a file called "skycoder.jpg" and had a password to be extracted.

First tried "Really? Again" from the things that I kept above but it didn't work.So then tried "Nothing Is As It Seems" and it worked!.

Then I checked it by typing <code>strings strings skycoder.jpg</code> but found nothing intresting...

After a while I decided to check the image a bit closer...

If you zoom the down right corner,you will see a red text which is the flag!

Flag: flag{hack_complete}
