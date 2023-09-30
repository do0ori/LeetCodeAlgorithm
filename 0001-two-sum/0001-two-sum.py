import bisect

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if target == 2 * num:
                if num == sorted_nums[i+1]:
                    idx = nums.index(num)
                    return [idx, nums.index(num, idx+1)]
                else:
                    continue
            if target-num in sorted_nums:
                return [nums.index(num), nums.index(target-num)]