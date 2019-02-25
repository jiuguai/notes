```python
import numpy as np
# 构建方法
arr = np.array([[1,2,3],('a','b','c')])
arr = np.arange(1,10,1)
arr = np.linspace(1, 5, num=20)
arr = np.zeros((2,2))
arr1 = np.ones((2,2))
arr = np.zeros_like(arr1)
arr = np.ones_like(arr1)
arr = np.eye(5) # N*N 单位矩阵
# 基本属性
arr.ndim
arr.shape
arr.size
arr.dtype
arr.itemsize
arr.data

# 基本方法
arr.reshape(3,6)
np.reshape(arr,(3,6)) # arr.size 与原先一致
np.resize(arr,(3,9))  # arr.size 可不一致
arr1 = arr.copy()
arr.astype('int64')

# 堆叠操作
arr.hstack((ar1,ar2)) # 对axis=1 进行堆叠 
arr.vstack((ar1,ar2)) # 对axis=0 进行堆叠
arr.stack((ar1,ar2),axis=3)  # 对 aixs默认0 在轴为3的位置创建 “新轴” 堆叠

# 拆分
np.hsplit(arr,2)  # 按列拆分成2份
np.vsplit(arr,2)  # 按行拆分成2份

# 产生随机数
np.random.normal(size=(4,4), scale=1, loc=0)
np.random.rand(*nums) #[0,1)
np.random.randn(*nums) # 正太分布 scale=1 loc=0
np.random.randint(low=1, high=5, size=(5,5)) # high==None [0,low), high!=None [low,high)

# 保存
file_name = '/xxx.npy'
np.save(file_name, arr)
arr = np.load(file_name)

file_name = '/xxx.txt'
np.savetxt(file_name,arr, delimiter=',')
arr = np.loadtxt(file_name, delimiter=',')

# 数据类型
bool
inti    # 根据系统判断
int8    # -128 ~ 127
int16   # -32768 ~ 32767
int32   # -2*31 ~ 2*31-1
int64   # -2*63 ~ 2*63-1
uint8   # 0 ~ 255
uint16  # 0 ~ 65535 
uint32  # 0 ~ 2*32-1
uint64  # 0 ~ 2*64-1
float16 # 16bit 1 5 10
float32 # 32bit 1 8 23
float64 # 64bit 1 11 52
complex64   # 实部 虚部各32bit
complex128  # ... 各64bit



```