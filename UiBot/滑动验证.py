import numpy as np
import cv2 as cv


bg = cv.imread()
front = cv.imread()

# 灰度化
bg = cv.cvtColor(bg, cv.COLOR_BGR2GRAY)

front = cv.cvtColor(front, cv.COLOR_BGR2GRAY)

#  逐行处理 每行有记录的时候就保留，否则社区
front = front[front.any(1)]


# 匹配图像
result = cv.matchTemplate(bg, front, cv.TM_CCOEFF_NORMED)

#  一维数组
arr = np.argmax(result)

# 更换为二维数组
x, y = np.unravel_index(arr,result.shape)

# 测试

w, h = front.shape
# 画框
cv.rectangle(bg, (y,x), (y+w, x+h), (38,38,38),2)


#  显示

cv.imshow('gray',bg)
cv.waitKey(0)


