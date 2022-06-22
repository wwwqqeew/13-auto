#!/usr/bin/python
# -*- coding: utf-8 -*-

import win32gui
import os
import os.path
import shutil

SW_HIDE = 0
SW_SHOW = 5
SW_MINIMIZE = 6
SW_SHOWMINNOACTIVE = 7
file_name = '_ReadMe.txt'
template_file = 'D:\\91_tools\\_ReadMe_template.txt'


def enumerationCallaback(hwnd, results):
    className = win32gui.GetClassName(hwnd)
    text = win32gui.GetWindowText(hwnd)
    # 找出地址栏
    if(className == 'ToolbarWindow32'):
        # change pattern if in no-chinese system
        pattern = '地址: '.decode('utf-8').encode('gb2312')
        if(text.find(pattern) >= 0):
            results.append(text[6:])


def get_path(path):
    for i in range(500):
    # while True:
        window = win32gui.GetForegroundWindow()
        if (window != 0):
            if (win32gui.GetClassName(window) == 'CabinetWClass'):
                win32gui.EnumChildWindows(window, enumerationCallaback, path)
                break
            else:
                # 使用python.exe执行python脚本的时候，会弹出控制台窗口，如下代码能把控制台置入后台
                if (win32gui.GetClassName(window) == 'ConsoleWindowClass'):
                    win32gui.ShowWindow(window, SW_MINIMIZE)

if __name__ == "__main__":
    # 获取当前窗口句柄(是一个整数)
    get_path("control")