class Solution(object):
    def twoSum(self, nums, target):
        for x, y in enumerate(nums):
            rem = target - y
            if rem in nums and nums.index(rem) != x:
                return [x, nums.index(rem)]


obj = Solution().twoSum([3,2,3], 6)
print(obj)