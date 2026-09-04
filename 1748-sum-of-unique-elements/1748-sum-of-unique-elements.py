class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=[]
        for num in nums:
            count=nums.count(num)
            if count==1:
                result.append(num)
        return sum(result)                