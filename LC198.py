class Solution(object):
    def rob(self, nums):
        last = 0 
        now = 0
        for i in nums: last, now = now, max(last + i, now)
        return now
