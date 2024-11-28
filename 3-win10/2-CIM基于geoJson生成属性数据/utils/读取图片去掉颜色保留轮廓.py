import os
import cv2
import numpy as np
from PIL import Image

def extract_contours(image_path, output_path , threshold1=100, threshold2=200):
    # 1. 读取图像并转换为灰度图
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. 使用 Canny 边缘检测提取轮廓
    edges = cv2.Canny(gray, threshold1, threshold2)

    # 3. 创建一个空白的黑色图像用于保存轮廓
    contour_image = np.zeros_like(img)

    # 4. 查找图像中的轮廓
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 5. 在空白图像上绘制轮廓
    cv2.drawContours(contour_image, contours, -1, (255, 255, 255), 1)

    # 6. 检查文件夹是否存在，不存在则创建
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"文件夹 {output_dir} 不存在，已创建")

    # 7. 保存提取轮廓后的图像
    cv2.imwrite(output_path, contour_image)

    # 显示轮廓图
    # Image.fromarray(contour_image).show()

    print(f"轮廓图已保存至：{output_path}")

# 使用示例
image_path = 'all.png'  # 输入图像路径
# image_path = 'map.png'  # 输入图像路径
out_image_name = 'output_contours.png'  # 输出图像名称
output_path = 'D:/test/2024-11-26/'  # 输出图像路径

# 两层循环提取轮廓，调整阈值threshold1和threshold2，每次添加10，直到255
for i in range(10, 255, 10):
    for j in range(10, 255, 10):
        output_path = f'D:/test/2024-11-26/{i}-{j}-{out_image_name}'
        extract_contours(image_path, output_path, i, j)
#
# # 提取轮廓
#
#

print('done')
