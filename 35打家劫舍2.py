class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if n==0:return 0
        if n==1:return nums[0]
        return max(maxRob[1:],maxRob[:-1])
    def maxRob(self, nums: List[int]) -> int:
        n= len(nums)
        if n==0:return 0
        if n==1:return nums[0]
        prev_cur,prev =0,nums[0]
        for i in range(2,n+1):
            cur = max(prev,prev_cur+nums[i-1])
            prev_cur,prev = prev,cur
        return prev