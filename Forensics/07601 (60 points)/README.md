https://mega.nz/#!CXYXBQAK!6eLJSXvAfGnemqWpNbLQtOHBvtkCzA7-zycVjhHPYQQ 

I think I lost my flag in there. Hopefully, it won't get attacked...

########################################################################

So the filewhich was downloaded,was a jpeg file.

So I executed <code>strings image_file_name.jpeg</code>

And analyzed it.

At some point I found this:

//////////////////////////////////////////////////////////////////////
__MACOSX/UX

 O^I
 
__MACOSX/Secret Stuff.../UX

 O^I
 
__MACOSX/Secret Stuff.../Don't Open This.../UX

        O^I
        
__MACOSX/Secret Stuff.../Don't Open This.../._I Warned You.jpegUX

cg`b`

!!AP&H

Secret Stuff.../UX

Secret Stuff.../.DS_StoreUX

        O^I
        
Secret Stuff.../Don't Open This.../UX

Secret Stuff.../Don't Open This.../.DS_StoreUX

        O^I
        
Secret Stuff.../Don't Open This.../I Warned You.jpegUX

 O^I
 
__MACOSX/UX

 O^I
 
__MACOSX/Secret Stuff.../UX

 O^I
 
__MACOSX/Secret Stuff.../Don't Open This.../UX
        O^Ip
        
__MACOSX/Secret Stuff.../Don't Open This.../._I Warned You.jpegUX

//////////////////////////////////////////////////////////////////////

So I tried to change the extension from .jpeg to .zip and it when opened it, I found the Secret Stuff folder!

So I got in it and it had another folder called "Don't Open This..." .

And inside it,it had another jpeg file.So I did this:

<code>strings I\ Warned\ You.jpeg | grep 'CTF'</code> and found the flag just like that!

Flag: ABCTF{Du$t1nS_D0jo}
