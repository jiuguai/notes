import numpy as np
import cv2 as cv


bg = cv.imread()
front = cv.imread()

bg = cv.cvtColor(bg, cv.COLOR_BGR2GRAY)

front = cv.cvtColor(front, cv.COLOR_BGR2GRAY)

#  处理滑块
front = front[front.any(1)]


# 匹配
result = cv.matchTemplate(bg, front, cv.TM_CCOEFF_NORMED)

np.argmax(result)

x, y = np.unravel_index(np.argmax(result),result.shape)

# 测试

w, h = front.shape
cv.rectangle(bg, (y,x), (y+w, x+h), (38,38,38),2)


#  显示

cv.imshow('gray',bg)
cv.waitKey(0)


