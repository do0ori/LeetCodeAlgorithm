class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 이전에 나온 합 개수
        sum_count = {0: 1}
        answer = 0
        s = 0
        for num in nums:
            s += num
            answer += sum_count.get(s - k, 0)
            sum_count[s] = sum_count.get(s, 0) + 1
        
        return answer