import time
import win32gui


def get_current_window():
    return win32gui.GetForegroundWindow()


def set_current_window(hwnd):
    win32gui.SetForegroundWindow(hwnd)


def get_window_title(hwnd):
    return win32gui.GetWindowText(hwnd)


def get_current_window_title():
    return get_window_title(get_current_window())


def find_window_by_title(title):
    try:
        return win32gui.FindWindow(None, title)
    except Exception as ex:
        print('error calling win32gui.FindWindow ' + str(ex))
        return -1

def enumerationCallaback(hwnd, results):
    className = win32gui.GetClassName(hwnd)
    text = win32gui.GetWindowText(hwnd)
    # 找出地址栏
    if(className == 'ToolbarWindow32'):
        # change pattern if in no-chinese system
        pattern = '地址: '.decode('utf-8').encode('gb2312')
        if(text.find(pattern) >= 0):
            results.append(text[6:])

if __name__ == "__main__":
    # 获取当前窗口句柄(是一个整数)
    print(get_current_window())
    # 获取当前窗口标题
    print(get_current_window_title())
    # 给定一个标题, 查找这个窗口, 如果找到就放到最前
    hwnd = find_window_by_title('control')
    set_current_window(hwnd)

    time.sleep(1)
    # 打印刚刚切换到最前的窗口标题
    print(get_current_window_title())

    enumerationCallaback(hwnd, [])


