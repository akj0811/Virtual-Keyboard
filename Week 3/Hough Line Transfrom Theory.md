# HOUGH TRANSFORM

Hough Transform is basically a feature extraction technique used in image analysis, computer vision and digital image processing. The aim is to find instances (though imperfect) of objects within a certian class of shapes governed by some sort of voting procedure. 

A very high level glimpse is that we transform our co-ordinates to a new parametric space. Using this, the objects that we are trying to search for are found as the local maxima in accumulator space contructed by the algorithm. 

Initially, the transform was aimed at extracting probable lines in the image but now it has been extended to identify some classes of shapes. 

One could argue that the edge detector can do the job of finding straight lines. Indeed, to some extent that works but that has certain limitations - 
* There can be missing points/pixels on the desired curve obtained using the edge detector.
* There can be devations between the actual curves and the desired curves that can lead to some sort of non-detectability. 

So, Hough Transform Algorithm helps to deal with these imperfections inherently present in the data or caused by the edge detector. This algorithm develops some sort of grouping of the edge pixels and based on the parameters set, tries to see if the desired object can be traced in the image depending on the explicit voting procedure that is undertaken. 

Let's now delve into the technical details of the Transform and the corresponding algorithm.

### Cartesian Form 
  The general equation of a straight line is given as by : *y = mx + c*. Now think about transforming it to the *(m, c)* space. How does the line look in the *(m, c)* space? That look like a point. And any general point on the line is a line in the *(m, c)* space. This can be realised by representing the equation in the following format : *c = -mx + y*, so the slope of this line is *x* and the intercept being *y*.  
  So this now gives a general idea to see if a line is present in the image or not. For all points on the edge, we draw the corresponding line on the *(m, c)* space and in the accumulator space, we obtain the votes i.e. the number of lines through it, of each co-ordinate of the *(m, c)* space. If it is more than some threshold, then a line with that *(m, c)* is said to exist in the image and that completes our job. 


  
  ![640px-Hough_transform_diagram svg](https://user-images.githubusercontent.com/55907159/79689144-7f2fab80-8270-11ea-80e4-2acc97e5711f.png)



  The above diagram gives some insights to what is actually going on. Bascially, this shows that the *(m, c)* with the highest number of votes is probably the object we are looking for. In this case, we see that (405, 60&deg;) is somewhat and optimal choice for the *(r, &theta;)* of the line.

  We can extend this idea to the *(r, &theta;)* space i.e. the Polar form using the Hesse Normal Form of a line : *r = xcos&theta; + ysin&theta;*. 

### Polar Form 
  The general equation of a line in normal form is : *r = xcos&theta; + ysin&theta;*. Now, each point on the line transformed into the *(r, &theta;)* space gives some sort of a sinusoidal curve in contrast to the line in the *(m, c)* space.
  In the same way as the cartesian form, we draw the sinusoids in the *(r, &theta;)* space and in the accumulator space, we obtain the votes i.e. the number of curves through it, of each co-ordinate of the *(r, &theta;)* space. If it is greater than some threshold value, then a line with *(r, &theta;)* exists on the image. 

The polar form is preferred over the cartesian form because of the fact that for vertical lines, the slope blows up and hence it is not possible to represent the line in *(m, c)* space, but that limitation doesn' show up in polar form.  

---

### References

* [Wikipedia](https://en.wikipedia.org/wiki/Hough_transform)
* [Youtube Video](https://www.youtube.com/watch?v=7m-RVJ6ABsY&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=32)
