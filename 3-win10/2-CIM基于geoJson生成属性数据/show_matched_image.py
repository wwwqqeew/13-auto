import pyautogui
from PIL import Image

import cv2

def show_matched_image(imgName, confidence=0.9):
    # 使用 pyautogui 查找屏幕上图像的位置
    location = pyautogui.locateOnScreen(imgName, confidence=confidence)

    if location is not None:
        print(f"匹配到图像，位置：{location}")

        # 获取匹配区域（坐标：left, top, width, height）
        left, top, width, height = location

        # 使用 PIL 打开图像文件
        img = Image.open(imgName)

        # 裁剪匹配区域
        cropped_img = img.crop((left, top, left + width, top + height))

        # 显示裁剪后的图像
        cropped_img.show()

    else:
        print("未找到图像!")

# 示例：使用指定的图像文件进行匹配
imgName = 'image.png'  # 你要匹配的图像文件路径
confidence = 0.9
show_matched_image(imgName, confidence)
