import cv2
import numpy as np
import argparse
import yaml

def apply_conv_kernel(img, kernel):
    """Applies a convolution kernel to an image.

    Args:
      img: The input image as a NumPy array.
      kernel: A NumPy array representing the convolution kernel.

    Returns:
      The filtered image as a NumPy array (8-bit unsigned).
    """
    filtered_img = cv2.filter2D(img, cv2.CV_8U, kernel)
    print(f"Applied kernel:\n{kernel}")
    return filtered_img

def load_image_grayscale(image_path):
  """Loads an image from the specified path in grayscale.

  Args:
    image_path: The path to the image file.

  Returns:
    The image as a NumPy array in grayscale
  """
  img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  if img is None:
    raise ValueError(f"Could not read image from {image_path}")
  return img

def load_kernel_from_yaml(config_path):
  """Loads a convolution kernel from a YAML configuration file.

  Args:
    config_path: The path to the YAML file containing the kernel definition.

  Returns:
    The kernel as a NumPy array.
  """
  with open(config_path, 'r') as f:
    config = yaml.safe_load(f)
  return np.array(config['kernel'])

def main():
    """
    Parses command-line arguments, loads kernel from YAML, and applies it to the image.
    """

    parser = argparse.ArgumentParser(description='Apply a convolution kernel to an image.')
    parser.add_argument('image_path', type=str, help='Path to the input image file')
    parser.add_argument('config_path', type=str, help='Path to the YAML configuration file')

    args = parser.parse_args()

    kernel = load_kernel_from_yaml(args.config_path)

    gray_img = load_image_grayscale(args.image_path)

    filtered_img = apply_conv_kernel(gray_img, kernel)
    
    # Display the images
    concatenated_img = np.concatenate((gray_img, filtered_img), axis=1)
    cv2.imshow("Grayscale and Filtered Images", concatenated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()