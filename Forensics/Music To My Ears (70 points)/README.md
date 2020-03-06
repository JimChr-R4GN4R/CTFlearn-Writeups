This audio file is supposed to say the flag, but it's corrupted! ): 

https://mega.nz/#!jexRzTzD!Fd3tD8ZcLquXJrsycMFUzozC9MHqaG-srUBfGREtL-0 

Can you fix it and input the flag?

#####################################################################

So the downloaded file is a .m4a file.

So after some research I found this video:

https://youtu.be/we8x0i89ll0

Here he opens with a hex editor the file and deletes everything from <code>mdap</code> and behind.

Then he saves the new m4a file and opens it with faad.

So and he gets the fixed file.

So I downloaded faad for linux from here:

http://linuxfromscratch.org/blfs/view/svn/multimedia/faad2.html

And installed it.

then I edited the corrupted file with a hex editor and did what he did in the video.

Then saved the new file and typed in terminal <code>faad sound_file_name.m4a</code>

and there was created a new .wav file. Then I opened it and it was spelling the flag!

Flag: CTFlearn{1_c4n_f1x_it}
