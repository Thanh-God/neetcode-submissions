from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # lưu giá trị và index

        for i, num in enumerate(nums):
            complement = target - num

            # nếu đã tồn tại số cần tìm
            if complement in seen:
                return [seen[complement], i]

            # lưu số hiện tại vào dictionary
            seen[num] = i
        