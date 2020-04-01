The KGB agent Boris Ivanov found the place where one of the criminals was hiding for a long time. 

Unfortunately the criminal disappeared and more than that he shredded the piece of paper with important information. 

Help Boris to restore it. 

Here is a bin with the strips of paper: https://mega.nz/#!KLR3gaYD!6qvqvopHKjjzZZ0HC6pnWjXw0Pw5Z9kgKdGQCMXeUb0 .

Boris is an experienced agent and he instantly realized that the size of the sheet was 500x500

############################################################################################

So downlaoded a .zip file and extracted it's content which were 500 .png files.

After opening some of them I understood that I should merge all of them vertically.

Then I thinked about `PIL` library...

I didn't knew though how to import many images in python script with PIL...

So after some research I found this: https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python#30228308

and used `dermen`'s script.

```
import numpy as np
import PIL

list_im = ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']
imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Vertical_merged_image.jpg' )
```
I tested it,but I was getting this error:
`AttributeError: module 'PIL' has no attribute 'Image'`

So I added this:
```
import numpy as np
import PIL
`from PIL import Image`
```

So we have our script that merges the images vertically.

Now we have to make our images list to import the photos...

I found this: https://stackoverflow.com/questions/27593227/listing-png-files-in-folder

But when made it work,I could not sort the `list_im` list properly.

So I decided to make my list with the help of bash:
```
number=1

for i in {1..499}
do
    echo "${i}.png" >> my_list.txt
done
```

Now I will add my code in our script...

```

```

Flag: flag{th3_KGB_l0v3s_CTF}
