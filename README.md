# machine-learning projects

Collection of all my machine learning projects 
# cv.py
my code performs a basic image processing pipeline on a sample grayscale image from SciPy. It first loads the “ascent” image and applies a vertical Sobel filter to detect edges, highlighting areas with significant vertical intensity changes. This is done by convolving the image with a 3×3 kernel and storing the filtered result. To enhance performance and prevent overflow, pixel values are clipped between 0 and 255. After edge detection, the image is downsampled by reducing its size to half in both dimensions using max pooling, which preserves the most prominent edge in each 2×2 pixel block. Finally, the original, filtered, and downsampled images are displayed side-by-side and saved into a single PNG file for easy visualization.
# building a cv model using tensorFlow
This code loads the Fashion MNIST dataset, normalizes the images, and trains a simple neural network to classify clothing items. After training, it evaluates the model's accuracy on test data. Then, it selects a test image, converts it back to a 0-255 pixel range, and applies Canny edge detection to highlight its edges. Finally, it displays and saves the edge-detected image.
# deep learning exercises
# Linear Model with Keras – Intro to Deep Learning Exercise
This notebook builds a simple linear model using Keras to fit a linear function to a dataset—essentially performing linear regression. It's part of the Intro to Deep Learning course and provides hands-on practice with Keras model building and training fundamentals.
 # deep neural networks
In this exercise, I built a deep neural network using TensorFlow's Sequential API by stacking multiple dense layers. Activation functions like ReLU were applied to hidden layers to introduce non-linearity, enabling the network to learn complex patterns. I explored two methods of applying activations — directly within the Dense layer and separately using Activation layers. Additionally, I visualized and experimented with alternative activations such as ELU, SELU, and Swish to understand their behavior.
# Stoschastic gradient decent
A fully connected feedforward neural network (MLP) built with Keras to predict vehicle fuel economy.
It has three hidden layers (128, 128, and 64 units) with ReLU activations and a linear output layer for regression.
The model is trained using stochastic gradient descent with the Adam optimizer (an adaptive form of SGD), minimizing mean squared error (MSE) loss over 200 epochs with a batch size of 128.
# Overfitting and Underfitting
predicting how popular a song is with spotify dataset
Overfitting occurs when the model learns noise from the training data, resulting in poor generalization to new data.
Underfitting happens when the model is too simple to capture the underlying patterns.
To address these issues, early stopping was applied to halt training once validation loss stopped improving, preventing overfitting and improving model performance.


 feel free to connect with me regarding the code and the project via comments or my e-mail at 223111a66e6@aiml.sreenidhi.edu.in
=======
 feel free to connect with me regarding the code and the project via comments or my e-mail at 223111a66e6@aiml.sreenidhi.edu.in
>>>>>>> 28a9318e6968341108a78a355871a1bca916466a
