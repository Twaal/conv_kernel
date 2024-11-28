# conv_kernel

This is a command-line program that applies a convolution kernel to an image.

## Usage

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Prepare a YAML configuration file:**

    Create a YAML file (e.g., `kernel_config.yaml`) with the following structure:

    ```yaml
    kernel:
      - [0.0625, 0.125, 0.0625]
      - [0.125,  0.25,  0.125]
      - [0.0625, 0.125, 0.0625]
    ```

    You can define different kernels in the YAML file.

3.  **Run the program:**

    ```bash
    python apply_conv_kernel.py <image_path> <config_path>
    ```

    Replace `<image_path>` with the path to your image file and `<config_path>` with the path to your YAML configuration file.

## Example (Windows)

```bash
python apply_conv_kernel.py images/Lena.jpg kernel_config.yaml

## Example (macOS / Linux)

```bash
python3 apply_conv_kernel.py images/Lena.jpg kernel_config.yaml