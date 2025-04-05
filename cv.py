import cv2
import numpy as np
from scipy.datasets import ascent
import matplotlib.pyplot as plt

# Load the image and convert to int to avoid overflow
i = ascent().astype(np.int32)

# Apply edge detection filter (Sobel)
i_transformed = np.copy(i)
size_x, size_y = i.shape
sobel_filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
weight = 1

for x in range(1, size_x - 1):
    for y in range(1, size_y - 1):
        output_pixel = 0.0
        for fx in range(3):
            for fy in range(3):
                output_pixel += i[x + fx - 1, y + fy - 1] * sobel_filter[fx][fy]
        output_pixel *= weight
        output_pixel = max(0, min(255, output_pixel))
        i_transformed[x, y] = output_pixel

# Downsample the filtered image (take max of 2x2 blocks)
new_x, new_y = size_x // 2, size_y // 2
newImage = np.zeros((new_x, new_y))
for x in range(0, size_x - 1, 2):
    for y in range(0, size_y - 1, 2):
        pixels = [
            i_transformed[x, y],
            i_transformed[x + 1, y],
            i_transformed[x, y + 1],
            i_transformed[x + 1, y + 1]
        ]
        newImage[x // 2, y // 2] = max(pixels)

# Plot and save all three images in a single PNG
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
titles = ['Original Image', 'Filtered (Edge Detection)', 'Downsampled']
images = [i, i_transformed, newImage]

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig("combined_output.png")
