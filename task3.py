from PIL import Image
import numpy as np
from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt

img = Image.open('lena.jfif')
data = np.asarray(img,dtype = float)
pro_data = data.reshape(-1,3)

centroid, label = kmeans2(pro_data, 20, minit = '++')
new = np.array(centroid[label], dtype = np.uint8)
new = new.reshape((data.shape))
new_img = Image.fromarray(new, 'RGB')
new_img.save('ankit.png')
new_img.show()