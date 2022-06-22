import pyautogui
import time
import xlrd
import pyperclip
import os
from loguru import logger

# 读取指定路径下的所有文件夹的名称，并且输出
if __name__ == '__main__':
    # path = 'D:\\10-bat\\HDvideo\\static\\camera\\module2'
    path = "D:\\0-南方数码\\5-文档\\2-系统功能说明\\11-变形检测\\1-文档\\建设工程变形监测\\软件调研相关文件20220616\\原始数据"
    # 循环读取path下的所有文件
    for root, dirs, files in os.walk(path):
        print(root.replace(path + "\\", ''))


