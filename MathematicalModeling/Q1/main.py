import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

def apply_gaussian_filter(image_path, num_iterations=3):
    image = cv2.imread(image_path)
    # image = laplacian_filter(image) # 拉普拉斯滤波
    # image = robert_filter(image) # Robert算子
    # image = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
    for _ in range(num_iterations):
        image = cv2.GaussianBlur(image, (3, 3), 0)
    upsampled_image = cv2.pyrUp(image)  # 添加上采样
    return image, upsampled_image

def apply_threshold(image, threshold_value=127):
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def laplacian_filter(image):
    h = image.shape[0]
    w = image.shape[1]
    image_new = np.zeros(image.shape, np.uint8)
    for i in range(1, h-1):
        for j in range(1, w-1):
            image_new[i][j] = 4*image[i][j].astype(int) - image[i + 1][j].astype(int) - image[i - 1][j].astype(int) - image[i][j + 1].astype(int) - image[i][j - 1].astype(int) 
    return image_new

def robert_filter(image):
    h = image.shape[0]
    w = image.shape[1]
    image_new = np.zeros(image.shape, np.uint8)
    for i in range(1, h-1):
        for j in range(1, w-1):
            image_new[i][j] = np.abs(image[i][j].astype(int)-image[i+1][j+1].astype(int)) + np.abs(image[i+1][j].astype(int)-image[i][j+1].astype(int))
    return image_new

input_dir = "C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test"
output_dir = "C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\2_Gaussian_test"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        filtered_image, upsampled_image = apply_gaussian_filter(input_path, num_iterations=2)
        binary_upsampled_image = apply_threshold(upsampled_image)
        binary_image = apply_threshold(filtered_image)
        # downsampled_binary_image = cv2.pyrDown(binary_image)  # 二值化后的图像下采样
        downsampled_upsampled_image = cv2.pyrDown(upsampled_image)  # 上采样后的图像下采样
        binary_downsampled_image = apply_threshold(downsampled_upsampled_image)
        downsampled_binary_upsampled_image = cv2.pyrDown(binary_upsampled_image)
        # cv2.imwrite(output_path, binary_image)

        original_image = cv2.imread(input_path)
        plt.figure(figsize=(15, 5))
        plt.subplot(1, 6, 1)
        plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')
        plt.subplot(1, 6, 2)
        plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
        plt.title('Filtered Image')
        plt.subplot(1, 6, 3)
        plt.imshow(cv2.cvtColor(upsampled_image, cv2.COLOR_BGR2RGB))
        plt.title('Upsampled Image')
        plt.subplot(1, 6, 4)
        plt.imshow(cv2.cvtColor(downsampled_upsampled_image, cv2.COLOR_BGR2RGB))
        plt.title('Downsampled Image')
        plt.subplot(1, 6, 5)
        plt.imshow(cv2.cvtColor(binary_upsampled_image, cv2.COLOR_BGR2RGB))
        plt.title('Binary Upsampled Image')
        plt.subplot(1, 6, 6)
        plt.imshow(cv2.cvtColor(downsampled_binary_upsampled_image, cv2.COLOR_BGR2RGB))
        plt.title('Downsampled Binary Upsampled Image')
        plt.show()
        
        plt.figure(figsize=(5, 5))
        plt.imshow(cv2.cvtColor(downsampled_binary_upsampled_image, cv2.COLOR_BGR2RGB))
        plt.title('Downsampled Binary Upsampled Image')
        plt.show()