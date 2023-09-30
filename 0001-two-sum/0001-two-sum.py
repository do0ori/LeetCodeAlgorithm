class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Build Hash Table (num : index)
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = i    # index is overwritten if there are duplicated numbers.

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]