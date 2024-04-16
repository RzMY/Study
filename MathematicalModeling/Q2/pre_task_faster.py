import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q2\\test_data\\b02547.jpg")
# img = cv2.imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q2\\test_data\\b02535.jpg")
# img = cv2.imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q2\\test_data\\b02531Z.jpg")

print(img.shape)

img_new = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_new, connectivity=8)
# regions = measure.regionprops(labels)

# 计算图像总像素数
total_pixels = img_new.shape[0] * img_new.shape[1]
print(total_pixels)

# 获取图片的横纵像素值
height, width = img_new.shape[:2]
# print("Image width:", width)
# print("Image height:", height)

# 计算面积阈值
min_area = total_pixels * 0.00035
max_area = total_pixels * 0.0015

import matplotlib.pyplot as plt

# 获取所有连通区域的面积
areas = stats[1:, cv2.CC_STAT_AREA]  # 排除背景

# 对面积进行排序
sorted_areas = sorted(areas)

# 绘制图像
plt.figure(figsize=(10, 6))
plt.plot(sorted_areas[:-1], marker='o')
plt.title('Area of Connected Components')
plt.xlabel('Component')
plt.ylabel('Area')
plt.grid(True)
plt.show()

# 遍历所有连通区域
for i in range(1, num_labels):  # 0 label is the background
    # 获取当前连通区域的统计信息
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]

    # 根据设定的条件判断该区域是否为干扰元素
    # if area < min_area or area > max_area:
    #     # 如果是干扰元素，将该区域填充为黑色
    #     img_new[labels == i] = 0

    # if area < 25/(340*340)*width*width or area > sorted_areas[-1] * 0.2:

    if area < sorted_areas[-1] * 0.04 or area > sorted_areas[-1] * 0.2:
        img_new[labels == i] = 0
        continue
    
    img_new[labels == i] = 255
    # euler_number = regions[i-1].euler_number
    # print(euler_number)    
    # euler_number = cv2.connectedComponentsWithStats(img_new_gray.astype(np.uint8), connectivity=8)[0] - 1

    # r = round(w/h,1)

    # 计算外接矩形
    # bounding_rect = (x, y, w, h)

    # if r == 1.0:
    #     img_new[labels == i] = 0

    # if euler_number < -128:
    #     img_new[labels == i] = 0
        
    # print(bounding_rect)
    
    # # 根据设定的条件判断该区域是否为干扰元素
    # if area or euler_number == 0 or euler_number == 1:  # 这里的条件需要根据实际情况进行调整
    #     # 如果是干扰元素，将该区域填充为黑色
    #     img_new[labels == i] = 0

    
    # 在图像上显示欧拉数
    # cv2.putText(img_new, str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# # 显示最终结果
cv2.imshow("Origin", img)
cv2.imshow("Final Processed Image", img_new)
# cv2.imwrite("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\test.jpg", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()