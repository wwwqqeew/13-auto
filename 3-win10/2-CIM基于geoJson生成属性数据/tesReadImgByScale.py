from PIL import Image
import time
import pyautogui

def resize_image(img_path, scale_factor):
    img = Image.open(img_path)
    new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
    return img.resize(new_size)

# 默认的分辨率
screen_width, screen_height = 1920, 1080
# 获取当前平米的分辨率
screen_width, screen_height = pyautogui.size()
# 计算缩放比例
scale_factor = screen_width / 1920
confidence = 0.9

print('这个是缩放比例', scale_factor , '这个是当前的分辨率', screen_width, screen_height)
# 使用调整后的图像进行识别
img_resized = resize_image('image.png', scale_factor)
location = pyautogui.locateCenterOnScreen(img_resized, confidence=confidence)

if location is None:
    # 降低置信度，每次降低0.05，重新识别
    for i in range(1, 5):
        confidence = confidence - i * 0.05
        location = pyautogui.locateCenterOnScreen(img_resized, confidence = confidence)
        print(confidence , '这个是获取的位置', location)
        if location is not None:
            break
if location is None:
    print('没有找到目标')
print('这个是获取的位置', location)

pyautogui.moveTo(location)

# 休眠10秒
time.sleep(10)
