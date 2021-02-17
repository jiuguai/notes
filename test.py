import numpy as np

sql = "insert into info values(%s)" %(",".join(np.repeat("%s",13)))
print(sql)


l = [[1],[2],[3],[4]]


print(l[1:-1])
