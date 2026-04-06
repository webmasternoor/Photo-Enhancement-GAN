import cv2
import matplotlib.pyplot as plt
import numpy as np

def adjust_brightness_contrast(image_path, brightness=10, contrast=2.3, output_path='modified_image.jpg'):
    """
    Load an image, adjust its brightness and contrast, and display the results side-by-side.
    
    Parameters:
    - image_path (str): Path to the input image file.
    - brightness (int): Value to be added to each pixel for brightness adjustment.
    - contrast (float): Multiplicative factor for contrast adjustment.
    - output_path (str): Path to save the modified image.
    
    The function performs the following:
    1. Loads the image from the specified path using OpenCV.
    2. Displays the original image using matplotlib.
    3. Adjusts the brightness and contrast using cv2.addWeighted function.
    4. Saves the modified image to the given output path.
    5. Displays the modified image using matplotlib.
    """
    
    # Load the image from the specified file path in BGR format (OpenCV default)
    image = cv2.imread(image_path)

    # Convert BGR to RGB for correct color display with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Plot the original image in the first subplot
    plt.subplot(1, 2, 1)
    plt.title("Original")
    plt.imshow(image_rgb)
    plt.axis('off')  # Hide axis

    # Adjust the brightness and contrast:
    # The cv2.addWeighted function computes:
    #    dst = src1 * alpha + src2 * beta + gamma
    # Here:
    #   alpha = contrast (scaling factor)
    #   beta = 0 (no second image weighted contribution)
    #   gamma = brightness (additive brightness offset)
    image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

    # Convert adjusted image to RGB for matplotlib display
    image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

    # Save the modified image to disk
    cv2.imwrite(output_path, image2)

    # Plot the adjusted image in the second subplot
    plt.subplot(1, 2, 2)
    plt.title("Brightness & Contrast")
    plt.imshow(image2_rgb)
    plt.axis('off')  # Hide axis

    # Display both images side-by-side
    plt.show()

# Example usage:
adjust_brightness_contrast('1.png')
