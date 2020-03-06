There's nothing I love more than oreos, lions, and winning. 

https://mega.nz/#!DC5F2KgR!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y Have Fun :)

################################################################################

So the downloaded file was a jpg.

Right away I did <code>binwalk image_file_name.jpg</code>

and got this result:

///////////////////////////////////////////////////////////////////////////

0             0x0             JPEG image data, JFIF standard 1.01
9515          0x252B          RAR archive data, version 4.x, first volume type: MAIN_HEAD

///////////////////////////////////////////////////////////////////////////

So I added .rar extention (image_file_name.jpg.rar) and extracted its content.

There was a folder with the name "1" and inside it, it had "a.txt" which was saying:

<code>This is not the flag you are looking for.</code>

and the second file was "b.jpg"

So I executed <code>strings b.jpg</code> and at the end found the flag!

Flag: flag{eat_more_oreos}
