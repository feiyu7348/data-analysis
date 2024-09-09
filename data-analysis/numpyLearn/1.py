import numpy as np

# 一维数组
data = np.array([1, 2, 3])
print(data)

# 二维数组
data = np.array([[1, 2, 3], [4, 5, 6]])
print(data)

# 全零数组
data = np.zeros(shape=(2, 3))
print(data)

# 全1数组
data = np.ones(shape=(2, 3))
print(data)

# 全空数组
data1 = np.empty(shape=(5, 3))
print(data1)

# 有连续序列的数组
data = np.arange(10, 16, 2)
print(data) # 数组从10开始步长为2，所以创建出来数组元素就是10，12，14

# 连续间隔的数组
data = np.linspace(10, 16, 3)
print(data) # 数组从10开始，步长为2，一共三个元素，所以创建出来数组元素就是10，12，14

# 创建随机数组
data = np.random.randint(10, 16, 3)
print(data) # 数组从10开始，
data = np.random.randint(10, 16, (2, 3))
print(data)