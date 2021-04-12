


def get_distance(image1,image2,threshold):  #滑块验证
    image1 = Image.open(image1)
    image2 = Image.open(image2)
    for i in range(65*image1.size[0]//260, image1.size[0]):
        for j in range(0, 150*image1.size[1]//260):
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))
            res_R = abs(pixel1[0] - pixel2[0])
            res_G = abs(pixel1[1] - pixel2[1])
            res_B = abs(pixel1[2] - pixel2[2])
            if res_R > threshold and res_G > threshold and res_B > threshold :
                i=i-11
                return i # 需要移动的距离
    return 10       