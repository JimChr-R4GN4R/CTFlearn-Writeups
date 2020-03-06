Here is a file with another file hidden inside it. 

Can you extract it? 

https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY

######################################################################

So from the link,we download a jpeg image.

From the title we see that we should use binwalk command.

So I executed this command: <code>binwalk image_file_name.jpeg</code>

and got this result:

///////////////////////////////////////////////////////////////////////////////////////

0             0x0             PNG image, 780 x 720, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
153493        0x25795         PNG image, 802 x 118, 8-bit/color RGBA, non-interlaced

///////////////////////////////////////////////////////////////////////////////////////

Here we see two PNGs...

So then executed this command: <code>binwalk -D 'png image:png' image_file_name.jpeg</code>

and get into the new folder which has been created.

And we find the two images and the second of them contains the flag!

Flag: ABCTF{b1nw4lk_is_us3ful}
