import numpy as np
import scipy
from matplotlib import image
import matplotlib.pyplot as plt
import scipy.ndimage

def convert_to_greyscale(fname, sigma_array=[4,10]):
    img = image.imread(fname)
    grey = np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])
    # grey = np.dot(img[...,:3], [0.5, 0.5, 0.5])
    grey_inverted = 255 - grey
    grey_inv_blurred = np.zeros_like(grey_inverted)
    for i in sigma_array:
        print(i)
        grey_inv_blurred += scipy.ndimage.filters.gaussian_filter(grey_inverted, sigma=i)
    grey_inv_blurred = grey_inv_blurred/len(sigma_array)
    # result = np.max(grey_inv_blurred, 255)
    result = np.minimum(grey_inv_blurred*255/(255-grey), 255.0)
    # result[grey==255]=255
    result = result.astype('uint8')
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.subplot(1,2,2)
    plt.imshow(result,cmap='gray')
    plt.show()

fname = r'C:\Users\703235761\Pictures\Saved Pictures\0.jfif'
me = r'C:\Users\703235761\Pictures\me.jpg'
convert_to_greyscale(me)