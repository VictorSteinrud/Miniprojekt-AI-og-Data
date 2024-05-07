from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.ndimage import uniform_filter


def gaussian_noise(image, mean=0, sigma=0.1):
    """
    Adds Gaussian noise to an image.
    
    Parameters:
    image : PIL.Image
        Image to which noise will be added.
    mean : float
        Mean of the Gaussian noise.
    sigma : float
        Standard deviation of the Gaussian noise.
    
    Returns:
    PIL.Image
        Image with Gaussian noise added.
    """
    # Convert image to numpy array
    im_array = np.array(image)
    
    # Generate Gaussian noise
    noise = np.random.normal(mean, sigma, im_array.shape)
    
    # Add the noise to the image
    noisy_image = im_array + noise * 255  # Scale the noise by 255 because image arrays are in [0, 255]
    
    # Ensure we don't go out of bounds in pixel values
    noisy_image = np.clip(noisy_image, 0, 255)
    
    # Convert back to an image
    noisy_image = Image.fromarray(noisy_image.astype('uint8'))
    
    return noisy_image

def apply_mean_filter(image, size=3):
    """
    Apply a mean filter to the image.
    :param image: Pillow Image object in grayscale
    :param size: Size of the kernel (size x size)
    """
    # Convert image to array
    img_array = np.array(image)
    # Apply uniform filter (mean filter)
    filtered_image = uniform_filter(img_array, size=size)
    # Convert array back to Image
    mean_filtered_image = Image.fromarray(filtered_image.astype(np.uint8))
    return mean_filtered_image

# Load an image
img = Image.open(r"C:\Users\Victor Steinrud\Pictures\Processed\grayscale_image.png").convert('RGB')
output_directory = r"C:\Users\Victor Steinrud\Pictures\Processed"

# Add Gaussian noise to the image
noisy_img = gaussian_noise(img, mean=0, sigma=0.1)


noisy_img = apply_mean_filter(noisy_img)
noisy_img.save(os.path.join(output_directory, "gaussian_noise_mean_filtered.png"))
# Display the original and noisy image
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(noisy_img)
plt.title('Image with Gaussian Noise')
plt.axis('off')

plt.show()