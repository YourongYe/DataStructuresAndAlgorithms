# Sort + Hashtable （只适用于sum=0的情况）
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        counter = collections.Counter(nums)
        if 0 in counter and counter[0] >= 3:
            res.append([0,0,0])
        
        pos = [n for n in counter if n > 0]
        neg = [n for n in counter if n < 0]
        neg.sort() # 这是辅助算法，可以提高time efficiency
        
        for p in pos:
            for n in neg:
                rem = -p - n
                if rem in counter:
                    if (rem == p or rem == n) and (counter[rem] >= 2):
                        res.append([rem, p, n])
                    elif n < rem < p:
                        res.append([rem, p, n])
                    elif rem < n: # 这两行为辅助算法部分，删除也不会错，只是会慢一些
                        break
        return res
```

# Sort + Two Pointers （适合所有3sum）
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 必须要先sort
        res = []
        target = 0 
        while target < len(nums)-2: # target即是选定的第一个数
            front = target + 1 # 接下来根据target来用two pointer确定另外两个数
            back = len(nums) - 1 # 一个从前开始，一个从后开始
            while front < back:
                sub_sum = nums[front] + nums[back]
                if sub_sum > -nums[target]:
                    back -= 1
                elif sub_sum < -nums[target]:
                    front += 1
                else:
                    triplet = [nums[target], nums[front], nums[back]] 
                    res.append(triplet) # 当三个数加和为0时，将结果append进去
                    # 这里是为了去掉front和back重复，一个从前，一个从后
                    while front < back and nums[front] == triplet[1]: front += 1 
                    while front < back and nums[back] == triplet[2]: back -= 1
            # 这里是检验target的重复
            while (target+1 < len(nums)) and (nums[target] == nums[target+1]):
                target += 1
            target += 1 # 一个loop完成，target移到下一个数
        return res
```

# 总结
题型： 寻找所有符合某个条件的subarray，要全部列举并且return  
做法： 这种题型的重点是要穷尽所有可能，并且不能重复 （所以一般来讲，都要sort）  
有时，题型也有变种，例如简单地，只是让我count所有可能结果；或者return 第一个符合条件的index之类的；做法可能会不同  
这种subarray题型中，列举所有可能的结果是最难的（不能重复的更更难）  
在列举之前，一定要有规定，比如只有在符合某些条件的情况下，才会将结果append到res中
