class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        count=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i]!=nums[j]:
                    for k in range(j+1,n):
                        if nums[i]!=nums[k] and nums[j]!=nums[k]:
                            count+=1
        return count                    