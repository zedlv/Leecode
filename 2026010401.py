#【热题100】01-两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = []
        for i in range(len(nums)):
            if target - nums[i] in num_list:
                return [num_map[target - nums[i]],i]
            num_map(nums[i],i)