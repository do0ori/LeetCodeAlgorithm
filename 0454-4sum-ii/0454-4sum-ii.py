class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_count = {}

        # nums1 + nums2의 합 빈도 저장
        for n1 in nums1:
            for n2 in nums2:
                s = n1 + n2
                sum_count[s] = sum_count.get(s, 0) + 1

        answer = 0

        # nums3 + nums4의 합을 돌면서
        for n3 in nums3:
            for n4 in nums4:
                s = n3 + n4
                # 반대 부호 합의 빈도를 answer에 추가
                answer += sum_count.get(-s, 0)
        
        return answer