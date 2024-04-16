import cv2
import numpy as np
import mtutils as mt
from scipy.spatial import ConvexHull

# 读取并分割图像
img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\w01637.jpg")
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\h02060.jpg")
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\b02581F.jpg")
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q2\\test_data\\b02519Z.jpg")
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q2\\test_data\\b02524.jpg")
lsc = cv2.ximgproc.createSuperpixelLSC(img)
lsc.iterate(10)
mask_lsc = lsc.getLabelContourMask()
label_lsc = lsc.getLabels()
number_lsc = lsc.getNumberOfSuperpixels()
mask_inv_lsc = cv2.bitwise_not(mask_lsc)
img_lsc = cv2.bitwise_and(img, img, mask=mask_inv_lsc)

# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用全局Otsu阈值
ret, _ = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
global_otsu = ret  # 获取全局Otsu阈值

# 初始化最终二值化图像
final_binarized_img = np.zeros_like(gray_img)

# 处理每个超像素
for label in range(number_lsc):
    superpixel_indices = label_lsc == label
    superpixel = gray_img[superpixel_indices]

    if superpixel.size == 0:
        continue

    # 计算当前超像素的平均灰度值
    mean_val = np.mean(superpixel)

    # 根据平均值和全局Otsu阈值进行二值化
    final_binarized_img[superpixel_indices] = 255 if mean_val > global_otsu else 0

# 使用Canny边缘检测
canny_final_binarized_img = cv2.Canny(final_binarized_img, 50, 150)

# # 结合Canny边缘到原图
# final = final_binarized_img + canny_final_binarized_img
final = final_binarized_img

contours, _ = cv2.findContours(canny_final_binarized_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 将轮廓转换为点集
points = np.vstack([contour.squeeze() for contour in contours])

# 计算凸包
hull = ConvexHull(points)

# 创建一个全黑的图像
mask = np.zeros_like(gray_img)

# 填充凸包的区域
cv2.fillPoly(mask, [points[hull.vertices]], 255)

# 对原图像进行反色操作
img_inverted = cv2.bitwise_not(final)

# 扩展final和img_inverted的形状
final_expanded = final[..., None]
img_inverted_expanded = img_inverted[..., None]

# 创建一个新的图像，凸包内部的区域为原图像的对应区域，外部的区域为反色图像的对应区域
img_new = np.where(mask[..., None] == 255, final_expanded, img_inverted_expanded)

# 显示图像
cv2.imshow("Inverted Outside Convex Hull", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()

# #设置卷积核
# kernel = np.ones((5,5), np.uint8)
 
# #图像闭运算
# result = cv2.morphologyEx(img_new, cv2.MORPH_TOPHAT, kernel)
 
# #显示图像
# cv2.imshow("src", img_new)
# cv2.imshow("result", result)
# cv2.waitKey(0)

# # 将闭运算的结果转换为二值化的掩码
# _, result_mask = cv2.threshold(result, 1, 255, cv2.THRESH_BINARY)

# # 翻转result_mask
# result_mask_inverted = cv2.bitwise_not(result_mask)

# # 扩展result_mask_inverted的形状
# result_mask_inverted_expanded = np.expand_dims(result_mask_inverted, axis=-1)

# # 将翻转后的result_mask添加到img_new上
# img_new = cv2.bitwise_and(img_new, img_new, mask=result_mask_inverted)

# # 显示图像
# cv2.imshow("Final Image", img_new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(final.astype(np.uint8), connectivity=8)

# # 遍历所有连通区域
# for i in range(1, num_labels):  # 0 label is the background
#     # 获取当前连通区域的统计信息
#     x = stats[i, cv2.CC_STAT_LEFT]
#     y = stats[i, cv2.CC_STAT_TOP]
#     w = stats[i, cv2.CC_STAT_WIDTH]
#     h = stats[i, cv2.CC_STAT_HEIGHT]
    
#     area = stats[i, cv2.CC_STAT_AREA]
    
#     euler_number = cv2.connectedComponentsWithStats(final.astype(np.uint8), connectivity=8)[0] - 1

#     # 计算外接矩形
#     bounding_rect = (x, y, w, h)

#     # 根据设定的条件判断该区域是否为干扰元素
#     if area < 50 or area > 1500 or euler_number != 1:  # 这里的条件需要根据实际情况进行调整
#         # 如果是干扰元素，将该区域填充为黑色
#         img_new[labels == i] = 0

#     # 在图像上显示欧拉数
#     cv2.putText(img_new, str(euler_number), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

from skimage import measure

# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\w01637.jpg")
# img_new = cv2.imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\test.jpg")
# img_new_gray = cv2.cvtColor(img_new)

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

# # 使用Canny边缘检测
# canny_img_new = cv2.Canny(img_new, 50, 150)

# # 移除img_new的额外的维度
# img_new_squeezed = np.squeeze(img_new)

# # 结合Canny边缘到原图
# final_img = img_new_squeezed + canny_img_new

# 显示图像
cv2.imshow("Enhanced Contours", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(img_new.astype(np.uint8), connectivity=8)
regions = measure.regionprops(labels)

# 计算图像总像素数
total_pixels = img_new.shape[0] * img_new.shape[1]
print(total_pixels)

# 获取图片的横纵像素值
height, width = img.shape[:2]
# print("Image width:", width)
# print("Image height:", height)

# 计算面积阈值
min_area = total_pixels * 0.00035
max_area = total_pixels * 0.009

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

    # 获取当前连通区域的轮廓
    contour = labels == i
    contour_coords = np.column_stack(np.nonzero(contour))
    # 计算最小外接矩形
    rect = cv2.minAreaRect(contour_coords)
    # 获取最小外接矩形的宽和高
    w, h = rect[1]

    # if area < 82 or area > max_area:
    if area < 82/(645*645)*(width*width) or area > max_area:
        img_new[labels == i] = 0

    euler_number = regions[i-1].euler_number
    # print(euler_number)    
    # euler_number = cv2.connectedComponentsWithStats(img_new_gray.astype(np.uint8), connectivity=8)[0] - 1
    # if w == 0 or h == 0:
    #     img_new[labels == i] = 0
    #     continue
    
    # r = round(w/h,1)
    # if r > 2 or r < 0.5:
    #     img_new[labels == i] = 0

    # if euler_number < -128:
    #     img_new[labels == i] = 0
    
    # # 根据设定的条件判断该区域是否为干扰元素
    # if area or euler_number == 0 or euler_number == 1:  # 这里的条件需要根据实际情况进行调整
    #     # 如果是干扰元素，将该区域填充为黑色
    #     img_new[labels == i] = 0

    
    # 在图像上显示欧拉数
    # cv2.putText(img_new, str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# 显示最终结果
cv2.imshow("Origin", img)
cv2.imshow("Final Processed Image", img_new)
# cv2.imwrite("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\test.jpg", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()