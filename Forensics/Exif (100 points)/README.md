If only the password were in the image?

https://mega.nz/#!SDpF0aYC!fkkhBJuBBtBKGsLTDiF2NuLihP2WRd97Iynd3PhWqRw 

You could really ‘own’ it with exif.

######################################################################

So the downloaded file is a .jpg .

So the first thing I did was <code>strings imag_file_name.jpg</code>

and then I got this at the beginning.

////////////////////////////////////

JFIF


Exif


0231


0100


flag{3l1t3_3x1f_4uth0r1ty_dud3br0}

////////////////////////////////////

Flag: flag{3l1t3_3x1f_4uth0r1ty_dud3br0}

=======================================================================

Another method as the challenge recommends is exif!

If we run <code>exiftool image_file_name.png</code>

Then we will see this at some point:

////////////////////////////////////////////////////////////////////

Components Configuration        : Y, Cb, Cr, -

Flashpix Version                : 0100

Owner Name                      : flag{3l1t3_3x1f_4uth0r1ty_dud3br0}

GPS Latitude Ref                : South

GPS Longitude Ref               : East

////////////////////////////////////////////////////////////////////

Flag: flag{3l1t3_3x1f_4uth0r1ty_dud3br0}
