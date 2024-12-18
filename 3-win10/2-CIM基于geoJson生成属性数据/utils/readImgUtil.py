# -*- coding: utf-8 -*-
import cv2
import pyautogui
import time
from PIL import Image
import numpy as np

# 读取图像并进行预处理
def preprocess_image(image_path):
    # 读取图像并转为灰度图
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 对图像进行高斯模糊处理
    # img = cv2.GaussianBlur(img, (5, 5), 0)


    # 对图像进行二值化处理，增强对比度
    # img：输入的灰度图像。
    # 127：阈值，决定哪些像素应该是白色（255），哪些应该是黑色（0）。
    # 255：大于阈值的像素值将被设置为最大值（255，即白色）。
    # cv2.THRESH_BINARY：二值化的类型，指定了普通的二值化操作。
    #     cv2.THRESH_BINARY_INV：反向二值化（大于阈值的像素值变为
    #     0，小于阈值的变为最大值）。
    #     cv2.THRESH_TRUNC：像素值大于阈值的将被设置为阈值。
    #     cv2.THRESH_TOZERO：大于阈值的保持原样，小于阈值的像素值变为
    #     0。
    #     cv2.THRESH_TOZERO_INV：小于阈值的保持原样，大于阈值的像素值变为
    #     0。
    # _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    return Image.fromarray(img)

# 获取图像位置
def get_location(imgName, confidence=0.9, showLog=True):
    # 预处理图像后再进行匹配
    processed_img = preprocess_image(imgName)

    # 将处理后的图像保存到本地
    processed_img.show()
    processed_img.save('processed_img.png')

    # 转换为 PIL 图像对应的 numpy 数组格式供 pyautogui 使用
    # processed_img = np.array(processed_img)

    # 使用 pyautogui 寻找图像的位置
    location = pyautogui.locateCenterOnScreen(processed_img, confidence=confidence)

    # 如果没有找到目标，调整 confidence 值进行重试
    if location is None:
        for i in range(1, 10):
            confidence = confidence - i * 0.1
            # location = pyautogui.locateCenterOnScreen(processed_img, confidence=confidence)
            location = pyautogui.locateOnScreen(processed_img, confidence=confidence)
            if location is not None:
                break

    # 如果仍未找到，打印日志并返回 None
    if location is None and showLog:
        print('没有找到目标')
    elif showLog:
        print(f"找到目标位置：{location}，当前置信度：{confidence}")

    return location, confidence  # 返回位置和调整后的confidence

# 调整图像大小
def resize_image(img_path, scale_factor):
    img = Image.open(img_path)
    new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
    return img.resize(new_size)

# 获取全屏截图
def capture_screen():
    # 使用 pyautogui 获取整个屏幕的截图
    screenshot = pyautogui.screenshot()
    return screenshot

# 显示匹配图像区域
def showImageByLocation(imgName, confidence):

    print(f"匹配图像{imgName}，参数：{confidence}")

    # 获取图像位置
    location = pyautogui.locateOnScreen(imgName, confidence=confidence)
    if location is not None:
        print(f"匹配到图像，位置：{location}")

        # 获取匹配区域（坐标：left, top, width, height）
        left, top, width, height = location

        # 获取全屏截图
        screenshot = capture_screen()

        # 裁剪匹配区域
        cropped_img = screenshot.crop((left, top, left + width, top + height))

        # 显示裁剪后的图像
        cropped_img.show()
    else:
        print("未找到匹配图像!")
    return location


# 主程序
# imgName = "D:\\test\\image.png"
imgName = "all.png"
confidence = 0.9

print(f'图片路径: {imgName}')

location, confidence = get_location(imgName, confidence)

if location:
    location = showImageByLocation(imgName, confidence)
    pyautogui.moveTo(location)
    print(f"鼠标已移动到位置: {location}")




# 休眠10秒，以便观察结果
# time.sleep(10)
