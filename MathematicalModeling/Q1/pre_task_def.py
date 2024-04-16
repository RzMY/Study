# import cv2
# import numpy as np
# import mtutils as mt

# # 读取并分割图像
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\h02060.jpg")
# lsc = cv2.ximgproc.createSuperpixelLSC(img)
# lsc.iterate(10)
# mask_lsc = lsc.getLabelContourMask()
# label_lsc = lsc.getLabels()
# number_lsc = lsc.getNumberOfSuperpixels()
# mask_inv_lsc = cv2.bitwise_not(mask_lsc)
# img_lsc = cv2.bitwise_and(img, img, mask=mask_inv_lsc)

# # cv2.imshow("Image", img_lsc)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # exit(0)
# # 转换为灰度图像
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 初始化最终二值化图像
# final_binarized_img = np.zeros_like(gray_img)

# # 处理每个超像素
# # for label in range(number_lsc):
# #     # 获取当前超像素的像素
# #     superpixel_indices = (label_lsc == label)
# #     superpixel = gray_img[superpixel_indices]
    
# #     if superpixel.size == 0:
# #         continue
    
# #     # 对当前超像素应用Otsu算法
# #     threshold, _ = cv2.threshold(superpixel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
# #     print(threshold)
# #     # 应用阈值，更新最终图像
# #     superpixel_binarized = np.zeros_like(superpixel)
# #     superpixel_binarized[superpixel >= threshold] = 255
# #     final_binarized_img[superpixel_indices] = superpixel_binarized

# # 处理每个超像素
# # 处理每个超像素
# for label in range(number_lsc):
#     # 获取当前超像素的像素
#     superpixel_indices = (label_lsc == label)
#     superpixel = gray_img[superpixel_indices]
    
#     if superpixel.size == 0:
#         continue
    
#     # 对当前超像素应用高斯滤波
#     superpixel_blurred = cv2.GaussianBlur(superpixel, (3, 3), 0)
    
#     # 对滤波后的超像素应用自适应阈值法
#     superpixel_binarized = cv2.adaptiveThreshold(superpixel_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    
#     # 将二维数组转换为一维数组
#     superpixel_binarized = superpixel_binarized.flatten()
    
#     final_binarized_img[superpixel_indices] = superpixel_binarized

# # 显示最终结果
# cv2.imshow("Final Binarized Image", final_binarized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import mtutils as mt

# # 读取并分割图像
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\w01637.jpg")
# lsc = cv2.ximgproc.createSuperpixelLSC(img)
# lsc.iterate(10)
# mask_lsc = lsc.getLabelContourMask()
# label_lsc = lsc.getLabels()
# number_lsc = lsc.getNumberOfSuperpixels()
# mask_inv_lsc = cv2.bitwise_not(mask_lsc)
# img_lsc = cv2.bitwise_and(img, img, mask=mask_inv_lsc)

# # 转换为灰度图像
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 初始化最终二值化图像
# final_binarized_img = np.zeros_like(gray_img)

# # 使用全局Otsu阈值
# ret, _ = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# global_otsu = ret  # 确保从cv2.threshold获得的是一个单一的阈值

# # 处理每个超像素
# for label in range(number_lsc):
#     superpixel_indices = label_lsc == label
#     superpixel = gray_img[superpixel_indices]

#     if superpixel.size == 0:
#         continue

#     # 计算当前超像素的平均灰度值
#     mean_val = np.mean(superpixel)

#     # 如果超像素的平均值大于全局Otsu阈值，则整个超像素设为白色，否则设为黑色
#     if mean_val > global_otsu:
#         final_binarized_img[superpixel_indices] = 255
#     else:
#         final_binarized_img[superpixel_indices] = 0

# canny_final_binarized_img = cv2.Canny(final_binarized_img, 50, 150)

# final = final_binarized_img + canny_final_binarized_img
# # 显示最终结果
# cv2.imshow("Final Binarized Image", final)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import mtutils as mt

# # 读取并分割图像
# # img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\w01637.jpg")
# # img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\h02060.jpg")
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\b02581F.jpg")
# lsc = cv2.ximgproc.createSuperpixelLSC(img)
# lsc.iterate(10)
# mask_lsc = lsc.getLabelContourMask()
# label_lsc = lsc.getLabels()
# number_lsc = lsc.getNumberOfSuperpixels()
# mask_inv_lsc = cv2.bitwise_not(mask_lsc)
# img_lsc = cv2.bitwise_and(img, img, mask=mask_inv_lsc)

# # 转换为灰度图像
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 使用全局Otsu阈值
# ret, _ = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# global_otsu = ret  # 获取全局Otsu阈值

# # 初始化最终二值化图像
# final_binarized_img = np.zeros_like(gray_img)

# # 处理每个超像素
# for label in range(number_lsc):
#     superpixel_indices = label_lsc == label
#     superpixel = gray_img[superpixel_indices]

#     if superpixel.size == 0:
#         continue

#     # 计算当前超像素的平均灰度值
#     mean_val = np.mean(superpixel)

#     # 根据平均值和全局Otsu阈值进行二值化
#     final_binarized_img[superpixel_indices] = 255 if mean_val > global_otsu else 0

# # 使用Canny边缘检测
# canny_final_binarized_img = cv2.Canny(final_binarized_img, 50, 150)

# # 结合Canny边缘到原图
# final = final_binarized_img + canny_final_binarized_img

# # 连通区域检测与填充小区域
# num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(final.astype(np.uint8), connectivity=8)

# # 遍历所有连通区域，填充小于50像素的区域
# for i in range(1, num_labels):  # 0 label is the background
#     if stats[i, cv2.CC_STAT_AREA] < 50:
#         final[labels == i] = 0  # 将面积小于50的区域设置为黑色

# # 显示最终结果
# cv2.imshow("Origin", img)
# cv2.imshow("Final Processed Image", final)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import mtutils as mt

# # 读取图像
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\b02581F.jpg")

# # 预处理
# lsc = cv2.ximgproc.createSuperpixelLSC(img)
# lsc.iterate(10)
# mask_inv_lsc = cv2.bitwise_not(lsc.getLabelContourMask())
# img_lsc = cv2.bitwise_and(img, img, mask=mask_inv_lsc)
# gray_img = cv2.cvtColor(img_lsc, cv2.COLOR_BGR2GRAY)

# # 全局Otsu阈值二值化
# _, thresholded_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # 使用Canny边缘检测
# edges = cv2.Canny(thresholded_img, 50, 150)
# cv2.imshow("6", thresholded_img)
# cv2.imshow("edges", edges)

# # 查找轮廓
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # 创建一个与原图同样大小的全黑图像，用于绘制凸包
# mask = np.zeros_like(gray_img)

# # 计算并绘制每个轮廓的最小凸包到掩码上
# for contour in contours:
#     hull = cv2.convexHull(contour)
#     cv2.drawContours(mask, [hull], -1, (255), thickness=cv2.FILLED)

# # 掩码反色，使凸多边形内部为0，外部为255
# mask_inv = cv2.bitwise_not(mask)

# # 使用掩码对原图进行反色操作，只影响凸多边形外部
# result_img = cv2.bitwise_and(img, img, mask=mask)  # 保留凸多边形内的原图
# outside = cv2.bitwise_and(img, img, mask=mask_inv)  # 获取凸多边形外的部分
# outside_inv = cv2.bitwise_not(outside)  # 反色凸多边形外的部分

# # 将未反色的凸多边形内部和反色的外部重新组合
# final_img = cv2.bitwise_or(result_img, outside_inv)

# # 显示结果
# cv2.imshow("Original Image", img)
# cv2.imshow("Processed Image", final_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# import mtutils as mt

# # 读取图像
# img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\b02581F.jpg")
# lsc = cv2.ximgproc.createSuperpixelLSC(img)
# lsc.iterate(10)
# label_lsc = lsc.getLabels()
# number_lsc = lsc.getNumberOfSuperpixels()

# # 转换为灰度图像并应用全局Otsu阈值二值化
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, thresholded_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # 初始化最终二值化图像
# final_binarized_img = np.zeros_like(gray_img)

# # 处理每个超像素
# for label in range(number_lsc):
#     superpixel_indices = label_lsc == label
#     superpixel = gray_img[superpixel_indices]

#     if superpixel.size == 0:
#         continue

#     # 计算当前超像素的平均灰度值
#     mean_val = np.mean(superpixel)

#     # 根据平均值和全局Otsu阈值进行二值化
#     final_binarized_img[superpixel_indices] = 255 if mean_val > thresholded_img else 0

# # 使用Canny边缘检测
# edges = cv2.Canny(final_binarized_img, 50, 150)

# # 查找轮廓
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # 创建掩码
# mask = np.zeros_like(gray_img)
# for contour in contours:
#     hull = cv2.convexHull(contour)
#     cv2.drawContours(mask, [hull], -1, 255, thickness=cv2.FILLED)

# # 掩码反色
# mask_inv = cv2.bitwise_not(mask)

# # 原图中保留凸多边形内部，对外部进行反色操作
# masked_img = cv2.bitwise_and(img, img, mask=mask)
# outside_inv = cv2.bitwise_and(img, img, mask=mask_inv)
# outside_inv = cv2.bitwise_not(outside_inv)  # 反色凸多边形外的部分
# final_img = cv2.add(masked_img, outside_inv)

# # 显示结果
# cv2.imshow("Original Image", img)
# cv2.imshow("Processed Image", final_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
import mtutils as mt

# 读取图像
img = mt.cv_rgb_imread("C:\\Users\\Administrator\\Documents\\Study\\Study\\MathematicalModeling\\Q1\\1_Pre_test\\b02581F.jpg")
lsc = cv2.ximgproc.createSuperpixelLSC(img)
lsc.iterate(10)
label_lsc = lsc.getLabels()
number_lsc = lsc.getNumberOfSuperpixels()

# 转换为灰度图像并应用全局Otsu阈值二值化
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
global_otsu, _ = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

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
edges = cv2.Canny(final_binarized_img, 50, 150)

# 查找轮廓
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 创建掩码
mask = np.zeros_like(gray_img)
for contour in contours:
    hull = cv2.convexHull(contour)
    cv2.drawContours(mask, [hull], -1, 255, thickness=cv2.FILLED)

# 反色掩码，这样掩码内部是黑色，外部是白色
mask_inv = cv2.bitwise_not(mask)

# 对凸多边形外部进行反色操作，保留内部
outside_img = cv2.bitwise_and(img, img, mask=mask_inv)  # 取得凸多边形外部
outside_inv = cv2.bitwise_not(outside_img)  # 反色凸多边形外的部分
inside_img = cv2.bitwise_and(img, img, mask=mask)  # 取得凸多边形内部

# 将反色的外部和未反色的内部重新组合
final_img = cv2.add(inside_img, outside_inv)

# 显示结果
cv2.imshow("Original Image", img)
cv2.imshow("Processed Image", final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()