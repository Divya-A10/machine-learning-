# machine-learning
Collection of all my machine learning projects 
# cv.py
my code performs a basic image processing pipeline on a sample grayscale image from SciPy. It first loads the “ascent” image and applies a vertical Sobel filter to detect edges, highlighting areas with significant vertical intensity changes. This is done by convolving the image with a 3×3 kernel and storing the filtered result. To enhance performance and prevent overflow, pixel values are clipped between 0 and 255. After edge detection, the image is downsampled by reducing its size to half in both dimensions using max pooling, which preserves the most prominent edge in each 2×2 pixel block. Finally, the original, filtered, and downsampled images are displayed side-by-side and saved into a single PNG file for easy visualization.
# building a cv model using tensorFlow
This code loads the Fashion MNIST dataset, normalizes the images, and trains a simple neural network to classify clothing items. After training, it evaluates the model's accuracy on test data. Then, it selects a test image, converts it back to a 0-255 pixel range, and applies Canny edge detection to highlight its edges. Finally, it displays and saves the edge-detected image.

 feel free to connect with me regarding the code and the project via comments or my e-mail at 223111a66e6@aiml.sreenidhi.edu.in
=======
 feel free to connect with me regarding the code and the project via comments or my e-mail at 223111a66e6@aiml.sreenidhi.edu.in
>>>>>>> 28a9318e6968341108a78a355871a1bca916466a
