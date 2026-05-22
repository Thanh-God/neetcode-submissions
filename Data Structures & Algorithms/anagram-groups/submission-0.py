from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            # tạo key bằng cách sắp xếp ký tự
            key = "".join(sorted(word))

            # nếu key chưa tồn tại thì tạo list rỗng
            if key not in groups:
                groups[key] = []

            # thêm từ vào nhóm
            groups[key].append(word)

        # trả về tất cả nhóm
        return list(groups.values())