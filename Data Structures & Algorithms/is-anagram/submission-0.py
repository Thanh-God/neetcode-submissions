class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Nếu độ dài khác nhau -> không phải anagram
        if len(s) != len(t):
            return False

        count = {}

        # Đếm ký tự trong s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Trừ ký tự theo t
        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            # Nếu số lần xuất hiện âm -> không hợp lệ
            if count[char] < 0:
                return False

        return True