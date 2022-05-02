import pyautogui
import time
import xlrd
import pyperclip
import os
from loguru import logger

#定义鼠标事件

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

def mouseClick(clickTimes,lOrR,img,reTry):
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片【"+img+"】,0.1秒后重试")
            time.sleep(0.5)
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.5)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.5)




# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮  7.0 按钮模拟
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(sheet1):
    checkCmd = True
    #行数检查
    if sheet1.nrows<2:
        print("没数据啊哥")
        checkCmd = False
    #每行数据检查
    i = 1
    while i < sheet1.nrows:
        # 第1列 操作类型检查
        cmdType = sheet1.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0 
        and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0 and cmdType.value != 7.0 and cmdType.value != 8.0):
            print('第',i+1,"行,第1列数据有毛病")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = sheet1.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value ==1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            if cmdValue.ctype != 1:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 模拟按键事件，内容不能为空
        if cmdType.value == 7.0:
            if cmdValue.ctype == 7:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 模拟方法体事件，内容不能为空
        if cmdType.value == 8.0:
            if cmdValue.ctype == 8:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        i += 1
    return checkCmd

#读取公共文件夹下的代码模块，并且运行
def runMethodBody(typename):
    try:
        print(os.path.abspath(os.path.join(os.getcwd(), "../..")) + "/0-common/" + typename + "/code.txt")
        f = open(os.path.abspath(os.path.join(os.getcwd(), "../..")) + "/0-common/" + typename + "/code.txt", "r",encoding='utf-8')  # 设置文件对象
        str = f.read()  # 将txt文件的所有内容读入到字符串str中
        exec(str)  # 运行代码
        f.close()  # 将文件关闭
    except Exception as r:
        print('错误 %s' %r)

# 日志记录
def readLog(logTxt):
    os.remove("runtime.log")
    logger.add("runtime.log")
    logger.debug(logTxt)
    os._exit()

#任务
def mainWork( sheet1):
    # 隐藏doc
    # f = open(os.path.abspath(os.path.join(os.getcwd(), "../.."))+"/0-common/隐藏自动处理窗口.txt", "r")  # 设置文件对象
    # str = f.read()  # 将txt文件的所有内容读入到字符串str中
    # exec(str) #运行代码
    # f.close()  # 将文件关闭
    # os.remove("runtime.log")
    # logger.add("runtime.log")

    # mouseClick(1, "left", "0.png", 1)

    k = 1
    while k < sheet1.nrows:
        print(sheet1.row(k)[0],sheet1.row(k)[1],sheet1.row(k)[2])
        k+=1

    # 开始执行表格数据读取

    i = 1
    while i < sheet1.nrows:
        #取本行指令的操作类型
        cmdType = sheet1.row(i)[0]
        if cmdType.value == 1.0:
            #取图片名称
            img = sheet1.row(i)[1].value
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(1,"left",img,reTry)
            print("单击左键",img)
        #2代表双击左键
        elif cmdType.value == 2.0:
            #取图片名称
            img = sheet1.row(i)[1].value
            #取重试次数
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(2,"left",img,reTry)
            print("双击左键",img)
        #3代表右键
        elif cmdType.value == 3.0:
            #取图片名称
            img = sheet1.row(i)[1].value
            #取重试次数
            reTry = 1
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0:
                reTry = sheet1.row(i)[2].value
            mouseClick(1,"right",img,reTry)
            print("右键",img) 
        #4代表输入
        elif cmdType.value == 4.0:
            inputValue = sheet1.row(i)[1].value
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)                                        
        #5代表等待
        elif cmdType.value == 5.0:
            #取图片名称
            waitTime = sheet1.row(i)[1].value
            time.sleep(waitTime)
            print("等待",waitTime,"秒")
        #6代表滚轮
        elif cmdType.value == 6.0:
            #取图片名称
            scroll = sheet1.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动",int(scroll),"距离")
        #7代表快捷键
        elif cmdType.value == 7.0:
            inputValue = sheet1.row(i)[1].value
            arr = inputValue.split('+')
            #按下按钮
            for oneKey in arr:
                pyautogui.keyDown(oneKey)
            #松开按钮
            for oneKey in arr:
                pyautogui.keyUp(oneKey)
            print("快捷键:",arr)
        #8代表执行方法体
        elif cmdType.value == 8.0:
            #取方法体名称
            methodBodyName = sheet1.row(i)[1].value
            print("方法体：",methodBodyName)
            runMethodBody(methodBodyName)

        i += 1

if __name__ == '__main__':
    file = 'cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    #通过索引获取表格sheet页
    sheetGet = wb.sheet_by_index(0)
    #数据检查
    checkCmd = dataCheck(sheetGet)
    print('开始执行程序')
    runMethodBody("隐藏自动处理窗口")
    mainWork(sheet1 = sheetGet)
