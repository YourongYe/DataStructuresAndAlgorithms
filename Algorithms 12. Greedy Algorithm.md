#  Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest   
sum and return its sum.

```py
def maxSubArray(self, nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1] # 这个for loop的output会变成：在第i位的数字是以原来的nums[i]为终点的subarray的所有集合中subarray的maximum sum
    for i in range(1, len(nums)): # 第二个for loop相当于算max（nums)，貌似要快一丢丢
        if nums[i] < nums[i-1]:
            nums[i] = nums[i-1]
    return nums[-1]
```
# Intermediate value
```py
[-2,1,-3,4,-1,2,1,-5,4]
[-2,1,-2,4,3,5,6,1,5] # 第一个for loop之后的nums
[-2,1,-3,4,-1,2,1,-5,4]
```
可以看出，第一个for之后的nums的每一位数都是subarray的maxium sum  
Eg. 4 就是所有以nums[3]为最后一位数的subarray中的maxium sum  
    6 就是[-1,1,-3,4,-1,2,1]这个array的所有subarray的sum的最大值 （前提是这些subarray都包含最后这一位数，否则不成立）
