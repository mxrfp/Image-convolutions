
# Image Convolution Processor

A Python-based command-line interface (CLI) application that applies mathematical convolution matrices (kernels) to images. 

This project was built to explore the fundamental mathematics behind image processing and computer vision. Instead of relying on pre-built filtering libraries (like OpenCV or SciPy), the core convolution algorithm is implemented entirely from scratch using standard NumPy array manipulation.

## Features

*   **Custom Convolution Engine:** Implements a 2D sliding-window convolution algorithm with automatic zero-padding.
*   **Grayscale Processing:** Automatically converts input images to 2D matrices (grayscale) for accurate mathematical processing.
*   **Multiple Kernels:** Includes a dictionary-dispatched menu with 5 pre-defined mathematical filters:
    *   Sharpen
    *   Box Blur
    *   Gaussian Blur
    *   Laplacian (Edge Detection)
    *   Emboss
*   **Safe I/O Operations:** Features automatic directory creation for outputs and robust user input handling.

## Technical Details

The core of the application is the `convolute(matrix, kernel)` function. 
It accepts an N x M image matrix and a 3x3 kernel. The algorithm dynamically pads the original matrix with zeros to preserve edge pixels, creates a static copy to prevent data mutation during calculation, and iterates through the grid applying the element-wise product and sum. Finally, boolean masking is used to clip the output values to the standard 8-bit range [0, 255].

## Prerequisites

To run this project, you need Python 3.x and the following libraries:

```bash
pip install numpy Pillow
```

## Usage

1. Clone the repository and navigate to the project directory.
2. Run the script via terminal:

```bash
python main.py
```

3. Provide the absolute or relative path to the image you want to process.
4. Select the desired filter from the interactive menu:

```text
----------------------------------------------------------------------------------------------------
                                          IMAGE CONVOLUTER                                          
----------------------------------------------------------------------------------------------------

[1]: Sharpen image
[2]: Box blur
[3]: Gaussian Blur
[4]: Laplacian
[5]: Emboss

Option: 
```

5. The processed image will be automatically saved in a newly created `results/` directory within the project folder.

## Future Improvements

*   **RGB Support:** Expanding the convolution engine to process 3-dimensional matrices (Red, Green, and Blue channels independently) to support color image filtering.
*   **Performance Optimization:** Replacing the native Python nested loops with vectorized operations or compiled C-extensions (like `scipy.signal.convolve2d`) to process high-resolution images in real-time.

