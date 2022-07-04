
"""
负索引：
    字符串，列表
"""
info = "abcdef"
print(info[-1])
nums = [1,2,3,4,5]
# [2, 3, 4] 从1位置往右取到 -1
print(nums[1:-1])
print(nums[::-1])


"""
打乱列表：
"""
import random
# 洗牌
random.shuffle(nums)
print(nums)