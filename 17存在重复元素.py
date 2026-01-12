from typing import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c_dict = Counter(nums)
        for dict in c_dict.values():
            if dict == 1:
                return True
        return False