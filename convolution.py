import numpy as np
from PIL import Image 
import os

def convolute(matrix, kernel):
    def padded(arry):
        size = arry.shape
        padded_array = np.zeros((size[0]+2, size[1]+2))
        padded_array[1:size[0]+1, 1:size[1]+1] = arry
        return padded_array
    
    if kernel.shape != (3,3):
        raise ValueError
    
    grid = padded(matrix)
    grid_copy = grid.copy()
    for row in range(grid.shape[0]-2):
        for col in range(grid.shape[1]-2):
            grid[0+row:3+row, 0+col:3+col][1, 1] =   \
                (grid_copy[0+row:3+row, 0+col:3+col]*kernel).sum()
    
    return grid[1:grid.shape[0]-1, 1:grid.shape[1]-1]


options = {
    "1": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]),
    "2": np.array([[1/9 for i in range(3)] for j in range(3)]),
    "3": np.array([[(1/16)*i for i in row] for row in [[1,2,1],[2,4,2],[1,2,1]]]),
    "4": np.array([[0,1,0],[1,-4,1],[0,1,0]]),
    "5": np.array([[-2,-1,0],[-1,1,1],[0,1,2]]),
    "6": np.array([[1/16, 2/16, 1/16], [2/16, 8/16, 2/16], [1/16, 2/16, 1/16]]),
    "7": np.array([[0,0,0],[-1,1,0],[0,0,0]]),
    "8": np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]),
    "9": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
    "10": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
    "11": np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]),
    "12": np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
    "13": np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

}
choice = None

title_len = 100
print("-"*title_len)
print("IMAGE CUNVOLUTER".center(title_len))
print("-"*title_len, end="\n\n")
print("[1]: Sharpen image", "[2]: Box blur", "[3]: Gaussian Blur", \
      "[4]: Laplacian","[5]: Emboss", "[6]: Glow", "[7]: Edge Enhance",\
        "[8]: High-Pass filter", "[9]: Sobel V", "[10]: Sobel H", "[11]: Prewitt"\
        ,"[12]: Shift", "[13]: Ridge" , sep="\n")
print()

while True:
    try:
        image = Image.open(input("file address: ").strip().replace("\"", ""))
        print("File was found! ")
        break
    except:
        print("File was not found / Is not valid")
        if input("Type 'exit' to exit(any other key to continue): ") == "exit":
            exit()
image = np.array(image.convert("L")).astype(float)


while True:
    choice = input("Option: ")
    if choice not in options.keys():
        print("choice is not valid")
        if input("Type 'exit' to exit(any other key to continue): ") == "exit":
            exit()
        continue
    break

print("Processing...")
image = convolute(image, options[choice]).astype(int)
image[image>255] = 255
image[image<0] = 0
image = Image.fromarray(image.astype(np.uint8))



target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
image.save(os.path.join(target_dir, "convoluted.png"), quality = 100)
print(f"Image saved in the folder {target_dir}")

input()



