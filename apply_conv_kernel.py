import cv2
import numpy as np
import argparse
import yaml

def apply_conv_kernel(image_path, kernel):
    """
    Applies a convolution kernel to an image.

    Args:
      image_path: Path to the input image file.
      kernel: A NumPy array representing the convolution kernel.

    Returns:
      The filtered image as a NumPy array.
    """

    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not read image from {image_path}")


    # Apply the kernel using filter2D
    filtered_img = cv2.filter2D(img, -1, kernel)

    return filtered_img

def main():
    """
    Parses command-line arguments, loads kernel from YAML, and applies it to the image.
    """

    parser = argparse.ArgumentParser(description='Apply a convolution kernel to an image.')
    parser.add_argument('image_path', type=str, help='Path to the input image file')
    parser.add_argument('config_path', type=str, help='Path to the YAML configuration file')

    args = parser.parse_args()

    # Load kernel from YAML file
    with open(args.config_path, 'r') as f:
        config = yaml.safe_load(f)
    kernel = np.array(config['kernel'])

    print(kernel)

    # Apply the kernel
    filtered_img = apply_conv_kernel(args.image_path, kernel)

    # Display the filtered image
    cv2.imshow('Filtered Image', filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()