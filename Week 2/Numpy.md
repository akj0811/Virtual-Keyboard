# Numpy Library

Numpy is a widely used library. It is of extensive use in the python programming. It's functions are of immense use in coding, they simplify our work and make the code look cleaner. The functions available in the library are very efficient making our codes really fast.

Here, I list down a few important functions and some notes related to the library.

 * **[numpy.squeeze()](https://www.geeksforgeeks.org/numpy-squeeze-in-python/)** :  `numpy.squeeze(arr, axis)`  
   | Parameters |  Functions  |
   | ---------- |  ---------  |
   | arr        | The array to be squeezed                                   |
   | axis       | Specifies the axis along which elements are to be squeezed |

    * It is used to remove the one-dimensional entries along the specified axis.
    * If the specified axis direction is not one-dimensional, then a Value-Error is raised.
 * **[numpy.linspace()](https://www.geeksforgeeks.org/numpy-linspace-python/)** :  `numpy.linspace(start, end, num)`  
   | Parameters |  Functions  |
   | ---------- |  ---------  |
   | start      | Starting element of the range   |
   | end        | Ending element of the range     |
   | num        | Number of elements in the range |
   
    * It is used to generate a range of a certain length and the set terminal elements.
   
 * **[numpy.fromfunction()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfunction.html)** :  `numpy.fromfunction(function, shape)`   
 
   | Parameters |  Functions  |
   | ---------- |  ---------  |
   | function   | The function from which the array is to be generated  |
   | shape      | The shape of the array                                |

   	* It is used to create an array by applying certain function on the indices of the array of any shape.
 * **[numpy.random.normal()](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.normal.html)** :  `numpy.random.normal(mean, std_deviation, shape)`  
 
   | Parameters    |  Functions  |
   | ------------- |  ---------  |
   | mean          | The mean of the distribution               |
   | std_deviation | The standard deviation of the distribution |
   | shape         | The shape of the array                     |
  
    * It returns an array of random numbers from the normal distribution with the set mean and standard deviation.
 

 * **[numpy.set_printoptions()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.set_printoptions.html)** :  ` numpy.set_printoptions(args)`  
 
 	  * It is used to set the various formatting options for the *print* statement.
 
 ``` python
import sys
import numpy as np 

a = np.arange(10000).reshape(100, 100)
np.set_printoptions(threshold = sys.maxsize)
print(a)
 ```

 * Deep Copy vs Shallow Copy - 
  	Shallow copy simply assigns a new variable name to the existing array. It means that the elements are copied as a reference. So, changing one array changes the other too.
  	Deep Copy copies the elements but they are stored at different memory locations. So, changing one array doesn't affect the other one.

 * *a\*b* denotes the element wise multiplication of the two numpy arrays whereas *a.dot(b)* represents matrix multiplication of the two arrays.

 * By default, the data type of numpy array is of the type float.

 * Writing *-1* in reshape means that the dimension is automatically calculated by using the other dimensions.
 * We can use integer/boolean arrays other than integers for array indices.

 * Linear algebra tools are also there in the library -
 	* numpy.linalg.inv(a)
 	* numpy.eye(n)
 	* a.transpose()
 	* numpy.linalg.eig(a)
