import cv2
import numpy as np

# 读取图像A（模板图像）和图像B（大图）
imageB = cv2.imread('all.png')  # 大图


# imageA = cv2.imread('imageA.png')  # 模板图像
# imageA = cv2.imread('image.png')  # 模板图像，扭曲，背景长
# imageA = cv2.imread('all-1.png')  # 模板图像，完全
# imageA = cv2.imread('image3.png')  # 模板图像，背景色改变
# imageA = cv2.imread('processed_img.png')  # 模板图像，只有轮廓同
# imageA = cv2.imread('image5.png')  # 模板图像，扭曲，背景短（这个也还是能对比出来的）
# imageA = cv2.imread('image6.png')  # 模板图像，扭曲变大223%，背景短
imageA = cv2.imread('image7.png')  # 模板图像，扭曲变小67%，背景短

# 如果想监测出来，那么背景图不能太长，尺寸最好差不多


# 转换为灰度图像，因为模板匹配通常在灰度图上进行
# grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

grayB = imageB
grayA = imageA

# 使用模板匹配，返回匹配结果矩阵
result = cv2.matchTemplate(grayB, grayA, cv2.TM_CCOEFF_NORMED)



# 获取匹配结果矩阵中最大值的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# max_loc 是匹配图像A在图像B中的位置
print(f"图像A在图像B中的位置：{max_loc}, 匹配度：{max_val}")

grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)


# 在图像B上绘制一个矩形框，标出图像A匹配到的位置
h, w = grayA.shape  # 获取模板图像的尺寸
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(imageB, top_left, bottom_right, (0, 0, 255), 2)

# 显示匹配结果
cv2.imshow('Matched Image', imageB)
cv2.waitKey(0)
cv2.destroyAllWindows()
