from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Đếm tần suất xuất hiện
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Sắp xếp theo số lần xuất hiện giảm dần
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Lấy k phần tử đầu
        result = []

        for i in range(k):
            result.append(sorted_freq[i][0])

        return result