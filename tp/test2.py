from PIL import Image
from PyQt5.QtWidgets import QApplication
#import PIL.Image as img
import pytesseract
import cv2
import win32api
import win32con
import win32gui
import pyautogui
import sys
import os
import time

def watermark_image(type):
    if type == 'txt':
        #创建一个txt
        open("test.txt","w+")
        #窗口打开txt，并最大化
        win32api.ShellExecute(1,'open',r'test.txt','','',3)
        time.sleep(2)
        #截取窗口图片
        hwnd = win32gui.FindWindow(None, "test.txt - 记事本")
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(hwnd).toImage()
        img.save("test.PNG")
        #关闭窗口删除txt
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        os.remove("test.txt")
        return "test.PNG"
    elif type == 'dask':
        #获取屏幕分辨率
        x_all = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y_all = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        #将屏幕分成9块，获取屏幕中间坐标
        x = w = x_all//3
        y = h = y_all//3
        print(x,y,w,h)
        img = pyautogui.screenshot(region=[x,y,w,h])
        img.save('dask.PNG')
        return "dask.PNG"
# 图片转换为文字
def image_str(path_image):
    image = Image.open(path_image)
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    Img = image.convert('L')
    #Img.save("11111.PNG")
    #gray = cv2.cvtColor(cv2.imread("11111.PNG"),cv2.COLOR_BGR2GRAY)
    #print(gray)
    # 自定义灰度界限，大于这个值为黑色，小于这个值为白色，现在水印可以用250
    threshold = 150
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 图片二值化
    photo = Img.point(table, '1')
    #photo.save("1111.PNG")
    # 逆时针旋转图片315度
    ng = photo.rotate(0)
    ng.save("11111.PNG")
    # 识别图片中的文字
    txt1 = pytesseract.image_to_string(ng,lang='chi_sim')
    # txt1 = pytesseract.image_to_string("D:/13-auto/tp/11111.PNG", lang='chi_sim')

    print(txt1)
    text=txt1.replace('\n', '').replace('\r', '').replace(' ', '')
    return text
if __name__=="__main__":
    strtest = image_str(watermark_image('txt'))
    print(strtest)
    result = "工作空间" in strtest
    print(result)