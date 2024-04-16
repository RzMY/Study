import cv2
import numpy as np
import mtutils as mt
from scipy.spatial import ConvexHull
from skimage import measure

img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\w01637.jpg")
img_new = cv2.imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\test.jpg")
img_new_gray = cv2.cvtColor(img_new, cv2.COLOR_BGR2GRAY)

# # 计算连通区域
# labels = measure.label(img_new_gray, connectivity=2)

# # 获取每个连通区域的属性
# regions = measure.regionprops(labels)

# i = 0
# # 遍历所有连通区域
# for region in regions:
#     # 获取当前连通区域的统计信息
#     minr, minc, maxr, maxc = region.bbox
#     area = region.area
#     euler_number = region.euler_number

#     # 计算外接矩形
#     bounding_rect = (minc, minr, maxc - minc, maxr - minr)

#     # 在图像上显示欧拉数
#     print(i)
#     i += 1
#     cv2.putText(img_new, str(euler_number), (minc, minr), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_new_gray.astype(np.uint8), connectivity=8)
regions = measure.regionprops(labels)

# 计算图像总像素数
total_pixels = img_new.shape[0] * img_new.shape[1]
print(total_pixels)

# 计算面积阈值
min_area = total_pixels * 0.00035
max_area = total_pixels * 0.009

# 遍历所有连通区域
for i in range(1, num_labels):  # 0 label is the background
    # 获取当前连通区域的统计信息
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]

    # 根据设定的条件判断该区域是否为干扰元素
    if area < min_area or area > max_area:
        # 如果是干扰元素，将该区域填充为黑色
        img_new[labels == i] = 0

    euler_number = regions[i-1].euler_number
    # print(euler_number)    
    # euler_number = cv2.connectedComponentsWithStats(img_new_gray.astype(np.uint8), connectivity=8)[0] - 1

    r = round(w/h,1)

    # 计算外接矩形
    bounding_rect = (x, y, w, h)

    # if r == 1.0:
    #     img_new[labels == i] = 0

    # if euler_number < -128:
    #     img_new[labels == i] = 0
        
    print(bounding_rect)
    
    # # 根据设定的条件判断该区域是否为干扰元素
    # if area or euler_number == 0 or euler_number == 1:  # 这里的条件需要根据实际情况进行调整
    #     # 如果是干扰元素，将该区域填充为黑色
    #     img_new[labels == i] = 0

    
    # 在图像上显示欧拉数
    cv2.putText(img_new, str(euler_number), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# 显示最终结果
cv2.imshow("Origin", img)
cv2.imshow("Final Processed Image", img_new)
# cv2.imwrite("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\test.jpg", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()