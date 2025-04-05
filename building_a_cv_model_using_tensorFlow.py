import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load Fashion MNIST dataset
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# Normalize images
training_images = training_images / 255.0
test_images = test_images / 255.0

# Build a simple neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile and train the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f"\nTest Accuracy: {test_accuracy:.4f}")

# Select an image to apply edge detection
image = (test_images[0] * 255).astype(np.uint8)  # Convert back to 0-255 scale
print("Original Test Image (0–255 values):")
print(image)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)
print("\nEdge-Detected Output (Canny Result):")
print(edges)

# Display the edge-detected image
plt.figure(figsize=(4, 4))
plt.imshow(edges, cmap='gray')
plt.title("Edge-Detected Output")
plt.axis('off')
cv2.imwrite("edge_detected_output.png", edges)
plt.show()
