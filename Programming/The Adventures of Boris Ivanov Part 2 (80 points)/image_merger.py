import numpy as np
import PIL
from PIL import Image

list_im = open("my_list.txt",'r')

list_im = list_im.read()

list_im = list(list_im.split('\n'))

list_im = list_im[:-1]

print(list_im)

imgs    = [ PIL.Image.open(i) for i in list_im ]

# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )



imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) ) # for vertical use 'vstack' and for horizontal use 'hstack'
imgs_comb = PIL.Image.fromarray( imgs_comb)
imgs_comb.save( 'Vertical_merged_image.png' )
