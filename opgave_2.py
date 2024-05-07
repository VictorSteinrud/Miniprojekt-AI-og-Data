from PIL import Image
import numpy as np
from scipy.ndimage import uniform_filter
import os

def load_and_convert_to_grayscale(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        grayscale_img = img.convert("L")
        return grayscale_img
def add_salt_pepper_noise(image, amount=0.05, salt_vs_pepper=0.5):
    """
    Add salt and pepper noise to an image.
    :param image: Pillow Image object in grayscale
    :param amount: Proportion of the image to replace with noise
    :param salt_vs_pepper: Proportional amount of salt vs. pepper noise
    """
    # Convert image to array
    img_array = np.array(image)
    # Calculate the number of pixels to change
    num_noise = int(amount * img_array.size)
    # Calculate the number of salt and pepper pixels
    num_salt = int(num_noise * salt_vs_pepper)
    num_pepper = num_noise - num_salt

    # Add Salt noise (white pixels)
    coords = [np.random.randint(0, i - 1, num_salt) for i in img_array.shape]
    img_array[coords[0], coords[1]] = 255

    # Add Pepper noise (black pixels)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in img_array.shape]
    img_array[coords[0], coords[1]] = 0

    # Convert array back to Image
    noisy_image = Image.fromarray(img_array)
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

# Example usage:
image_path = r"C:\Users\Victor Steinrud\Pictures\Lenna_(test_image).png"
output_directory = r"C:\Users\Victor Steinrud\Pictures\Processed"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

grayscale_image = load_and_convert_to_grayscale(image_path)
grayscale_image.save(os.path.join(output_directory, "grayscale_image.png"))  # Save the grayscale image

noisy_image = add_salt_pepper_noise(grayscale_image)
noisy_image.save(os.path.join(output_directory, "noisy_image.png"))  # Save the image with noise

mean_filtered_image = apply_mean_filter(noisy_image)
mean_filtered_image.save(os.path.join(output_directory, "mean_filtered_image.png"))  # Save the filtered image