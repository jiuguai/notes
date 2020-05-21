

# https://digi.bib.uni-mannheim.de/tesseract/
# 


import numpy as np

from PIL import Image
import pytesseract



def to_gray(img):

    return img.convert('L')

def noise_remove_pil(img, k):
    """
    8邻域降噪
    Args:
        image_name: 图片文件命名
        k: 判断阈值

    Returns:

    """

    def calculate_noise_count(img_obj, w, h):
        """
        计算邻域非白色的个数
        Args:
            img_obj: img obj
            w: width
            h: height
        Returns:
            count (int)
        """
        count = 0
        width, height = img_obj.size
        for _w_ in [w - 1, w, w + 1]:
            for _h_ in [h - 1, h, h + 1]:
                if _w_ > width - 1:
                    continue
                if _h_ > height - 1:
                    continue
                if _w_ == w and _h_ == h:
                    continue
                if img_obj.getpixel((_w_, _h_)) < 230:  # 这里因为是灰度图像，设置小于230为非白色
                    count += 1
        return count


    # 灰度
    gray_img = img.convert('L')

    w, h = gray_img.size
    for _w in range(w):
        for _h in range(h):
            if _w == 0 or _h == 0:
                gray_img.putpixel((_w, _h), 255)
                continue
            # 计算邻域非白色的个数
            pixel = gray_img.getpixel((_w, _h))
            if pixel == 255:
                continue

            if calculate_noise_count(gray_img, _w, _h) < k:
                gray_img.putpixel((_w, _h), 255)
    return gray_img



def to_binary(img, threshold=115):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img_binary = img.point(table,'1')
    return img_binary


if __name__ == '__main__':
    file_path = r"C:\Users\zero\Desktop\pic\t.jpg"

    img = Image.open(file_path)
    img = to_gray(img)
    img = noise_remove_pil(img,4)
    img = to_binary(img)
    img.save("x.png")
    pytesseract.image_to_string("x.png")

    # lang 词库选择
    pytesseract.image_to_string("x.png",lang='eng.my')