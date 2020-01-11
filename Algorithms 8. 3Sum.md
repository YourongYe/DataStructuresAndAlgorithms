# Sort + Hashtable
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

# Sort + Two Pointers
```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        target = 0 
        while target < len(nums)-2:
            front = target + 1
            back = len(nums) - 1
            while front < back:
                sub_sum = nums[front] + nums[back]
                if sub_sum > -nums[target]:
                    back -= 1
                elif sub_sum < -nums[target]:
                    front += 1
                else:
                    triplet = [nums[target], nums[front], nums[back]]
                    res.append(triplet)
                    while front < back and nums[front] == triplet[1]: front += 1
                    while front < back and nums[back] == triplet[2]: back -= 1
            while (target+1 < len(nums)) and (nums[target] == nums[target+1]):
                target += 1
            target += 1
        return res
```
