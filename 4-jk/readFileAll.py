import pyautogui
import time
import xlrd
import pyperclip
import os
from loguru import logger

# 读取指定路径下的所有文件夹的文件，并且输出“文件名称”和“文件内容”（读取的只能是可以以txt方式打开的）
if __name__ == '__main__':
    #path = 'D:\\10-bat\\HDvideo\\static\\camera\\module2'
    path = "D:\\0-南方数码\\5-文档\\2-系统功能说明\\5-数据融合（海洋风电厂）\\3-相关文档\\6-代码\\智慧网格\\前端"

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


    
