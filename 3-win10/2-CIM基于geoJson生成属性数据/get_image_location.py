import cv2
import numpy as np

from readImgUtil import preprocess_image


# 对比两张图像，找到图像A在图像B中的位置
def find_image_in_image(imageA_path, imageB_path, threshold=0.9):
    # 读取图像A和图像B
    imageB = cv2.imread(imageB_path)
    imageA = cv2.imread(imageA_path)

    # 转为灰度图像进行模板匹配
    imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配进行查找
    result = cv2.matchTemplate(imageB_gray, imageA_gray, cv2.TM_CCOEFF_NORMED)

    # 找到匹配区域，返回位置
    loc = np.where(result >= threshold)

    # 如果找到了匹配位置
    if loc[0].size > 0:
        print(f"图像A在图像B中的位置：{loc}")

        # 获取匹配位置的坐标 (左上角)
        top_left = (loc[1][0], loc[0][0])
        bottom_right = (top_left[0] + imageA.shape[1], top_left[1] + imageA.shape[0])

        # 在图像B上标出匹配位置
        cv2.rectangle(imageB, top_left, bottom_right, (0, 255, 0), 2)

        # 显示匹配后的图像
        cv2.imshow('Matched Image', imageB)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return top_left  # 返回图像A在图像B中的位置

    else:
        print("未在图像B中找到图像A")
        return None


# 图像A和图像B路径
imageA_path = "all-1.png"  # 图A的路径
imageB_path = "all.png"  # 图B的路径

# 调用函数
# find_image_in_image(imageA_path, imageB_path)

preprocess_image