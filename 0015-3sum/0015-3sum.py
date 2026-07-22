class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        N = len(nums)
        for i in range(N):
            # skip dupicate number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            total = -nums[i]
            j = i + 1
            k = N - 1
            while j < k:
                if nums[j] + nums[k] == total:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j <= k and nums[j] == nums[j - 1]:
                        j += 1
                    while j <= k and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[j] + nums[k] < total:
                    j += 1
                    while j <= k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j <= k and nums[k] == nums[k + 1]:
                        k -= 1
        return result
