import pytesseract
from PIL import Image


def demo():
    # 打开要识别的图片
    # image = Image.open('D:/13-auto/tp/11111.PNG')
    image = Image.open('D:/test/test.png')
    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image, lang='eng')

    # 输入所识别的文字
    print('这是识别的文字' , text)


if __name__ == '__main__':
    demo()

