
nums = [1,34,12,34,2,23,4,56,6,67]
# 这个sort对原列表直接进行排序 sort返回的是none
nums.sort()
print(nums)

# 列表中有字典怎么进行排序
nums1 = [
    {
        "name": "lianglong",
        "age": 30
    },
    {
        "name": "xiaohong",
        "age": 40
    },
    {
        "name": "xiaogang",
        "age": 23
    }
]
print(nums1)
"""
    调用sort后会将nums1中的对象当做参数传给key引用的函数
"""
nums1.sort(key=lambda item: item["age"])
print(nums1)