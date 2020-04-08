# Numpy Library

 * **[numpy.squeeze()](https://www.geeksforgeeks.org/numpy-squeeze-in-python/)** :
   **Parameters** - 
   		* arr - array-like (input array)
   		* axis - None/int/tuple of ints (optional)

   	**Output** - 
   	It returns all or subset of the given array. It basically removes the one - dimensional entries along the specified axis.
   	**Error** - 
   	If the specified axis direction is not one-dimensional, then a Value-Error is raised. 

 * **[numpy.set_printoptions]()** :
 	By default, when an array is printed, if the size of the array is too large to fit entirely in the screen, then the middle elements are skipped while printing. By using this function, the entire array is printed on the terminal when the array is invoked.
 
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

 * a(asterisk)b denotes the element wise multiplication of the two numpy arrays.
   a.dot(b) represents matrix multiplication of the two arrays.

 * numpy.random.random()(asterisk)mu + sigma returns random values from the normal distribution with sigma as the mean and mu as the standard deviation.
 * By default, the data type of numpy array is of the type float.
 * **[numpy.linspace]()** :
   **Parameters** :
   		* (start of range, end of range, number of elements required)

 * We can use integer/boolean arrays other than integers for array indices.
 * **[numpy.fromfunction]()** :
   ** Parameters** :
   		function - the function from which the array is to be generated.
   		shape - the shape of the array

   	It is used to create an array by applying certain function on the indices of the array of any shape.

 * Writing -1 in reshape means that the dimension is automatically calculated by using the other dimensions.

 * Linear algebra tools are also there in the library - 
 		* numpy.linalg.inv(a)
 		* numpy.eye(n)
 		* a.transpose()
 		* numpy.linalg.eig(a)
