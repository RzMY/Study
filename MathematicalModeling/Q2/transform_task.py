import os
import cv2

def apply_threshold(image, threshold_value=127):
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def pre_task(image, num_iterations=3):

    # rgb转灰度
    img_new = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_new, connectivity=8)
    
    areas = stats[1:, cv2.CC_STAT_AREA]
    sorted_areas = sorted(areas)
    
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area < sorted_areas[-1] * 0.04 or area > sorted_areas[-1] * 0.2:
            img_new[labels == i] = 0
            continue
    
        img_new[labels == i] = 255
        
    # 灰度转rgb
    image = cv2.cvtColor(img_new, cv2.COLOR_GRAY2BGR)

    return image

# 源文件夹和目标文件夹的路径
source_dir = 'C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q2\\test_data'
target_dir = 'C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q2\\test_data_tasked'  # 替换为你的目标文件夹路径

# 获取源文件夹中的所有文件名
filenames = os.listdir(source_dir)

# 对于源文件夹中的每个文件
for filename in filenames:
    # 读取图像
    image = cv2.imread(os.path.join(source_dir, filename))
    
    # 对图像应用pre_task函数进行预处理
    processed_image = pre_task(image)
    
    # 将处理后的图像保存到目标文件夹中
    cv2.imwrite(os.path.join(target_dir, filename), processed_image)
    
print("Done")