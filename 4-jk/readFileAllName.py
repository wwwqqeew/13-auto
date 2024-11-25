import pyautogui
import time
import xlrd
import pyperclip
import os
from loguru import logger


if __name__ == '__main__':
    #path = 'D:\\10-bat\\HDvideo\\static\\camera\\module2'
    path = "D:\\4-project\\island-base-point-project\\island-management-preject\\sea-island-manage\\src\\main\\java\\com"
    #循环读取path下的所有文件
    for root, dirs, files in os.walk(path):
        for file in files:
            #获取文件路径
            filePath = os.path.join(root, file)
            #获取文件名称
            fileName = os.path.basename(filePath)
            #输出文件名称
            print("/************************"+fileName+"************/")
            #输出文件内容
            with open(filePath, 'r', encoding='utf-8') as f:
                print(f.read())


    
