import cv2
import numpy as np

# 读取图像A（模板图像）和图像B（大图）
imageB = cv2.imread('imageB.png')  # 大图
imageA = cv2.imread('imageA.png')  # 模板图像

# 转换为灰度图像，因为模板匹配通常在灰度图上进行
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

# 使用模板匹配，返回匹配结果矩阵
result = cv2.matchTemplate(grayB, grayA, cv2.TM_CCOEFF_NORMED)

# 获取匹配结果矩阵中最大值的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# max_loc 是匹配图像A在图像B中的位置
print(f"图像A在图像B中的位置：{max_loc}, 匹配度：{max_val}")

# 在图像B上绘制一个矩形框，标出图像A匹配到的位置
h, w = grayA.shape  # 获取模板图像的尺寸
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(imageB, top_left, bottom_right, (0, 0, 255), 2)

# 显示匹配结果
cv2.imshow('Matched Image', imageB)
cv2.waitKey(0)
cv2.destroyAllWindows()
