# Computational Photography - lab 5
### Filip Gromuł

In this assignment we were supposed to use a large dataset of face images to colorize a set of grayscale face images.

As I have recently stumbled upon the newly-opensourced google library [tensorflow](http://tensorflow.org/) for large-scale numerical computations in machine learning, I took this opportunity to test the library doing this exercise.

The assignment took me about 6 hours, but it probably would have taken less if I didn't need to learn a new library while doing it.

Running times were a few minutes for the initial images loading and grayscale descriptors computation, 5 seconds for the PCA, and then about 2 seconds for finding and colorizing each image (with all descriptors already in memory).

I have chosen to perform the color transfer by converting the colored image to the HSV color space, and swapping it's V channel for the grayscale image, obtaining pretty decent results.

Better results yet could be obtained by using a well-researched color transfer algorithm, such as [this](https://github.com/jrosebr1/color_transfer).

I have performed the Principal Component Analysis with 20 components and the results were suprisingly good.
There were some artifacts when compared to the 32x32 descriptors, but it was very insightful to see that such a large reduction in dimensionality may still provide satisfactory results.