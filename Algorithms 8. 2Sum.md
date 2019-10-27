# Brute Force
```py
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

# Two-pass Hash Table
```py
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic.keys() and dic[complement] != i:
                return [i, dic[complement]]
```
# One-pass Hash Table (most efficient both time and space complexity)
```py
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                return [i, dic[nums[i]]]
            complement = target - nums[i]
            dic[complement] = i
                    
  ```          
