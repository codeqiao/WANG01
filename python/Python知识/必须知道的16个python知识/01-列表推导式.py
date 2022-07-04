# 为什么使用列表推导式
## 如果有一个列表，这个列表中有1-10
## 方式1（简单明了，但是代码有太多的冗余）


nums = []
nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
nums.append(6)
nums.append(7)
nums.append(8)
nums.append(9)
nums.append(10)
print(nums)

## 方式2 for循环
nums1 = []
for i in range(10):
    nums1.append(i+1)
print(nums1)

## 方式3 列表推导式
## 列表推导式for循环是控制次数，for循环左边的是值
nums2 = [i+1 for i in range(10)]
print(nums2)


## 扩展练习
## 0-10中的偶数
nums3 = [ i for i in range(1,11) if(i%2==0)]
print(nums3)

##　快速生成 【“data0”,"data1"...】
datas = ["data{}".format(i) for i in range(10)]
print(datas)

##  快速生成 ["data0","gy1","data2","gy3"...]
datasgys = []
for i in range(100):
    if i%2 == 0:
        datasgys.append("data{}".format(i))
    else:
        datasgys.append("gy{}".format(i))
print(datasgys)
## 列表推导式
datasgys1 = ["data{}".format(i) if i%2==0 else "gy{}".format(i) for i in range(100)]
print(datasgys1)

