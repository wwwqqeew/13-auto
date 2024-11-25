import cv2
import pyautogui
import time
from PIL import Image

def preprocess_image(image_path):
    # 读取图像并转为灰度图
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 对图像进行二值化处理，增强对比度
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return Image.fromarray(img)


imgName = 'image.png'
# 输出图片绝对路径
print('这个是图片的绝对路径',imgName)
# 预处理图像后再进行匹配
processed_img = preprocess_image(imgName)

location = pyautogui.locateCenterOnScreen(processed_img, confidence=0.9)
# 如果没有找到目标，location为None，则切换参数confidence的值
if location is None:
    for i in range(1, 10):
        location = pyautogui.locateCenterOnScreen(processed_img, confidence=0.9 - i * 0.1)
        if location is not None:
            break
if location is None:
    print('没有找到目标')
print(' 这个是获取的位置',location)


pyautogui.moveTo(location)

# 休眠10秒
time.sleep(10)