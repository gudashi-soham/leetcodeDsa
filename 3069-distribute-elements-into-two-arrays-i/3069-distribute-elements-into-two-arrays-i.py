class Solution(object):

    def resultArray(self, nums):
        """
        :type nums: List[int]

        :rtype: List[int]
        """
        
        result1 = [nums[0]]
        result2 = [nums[1]]

        
        for i in range(2, len(nums)):
            if result1[-1] > result2[-1]:
                result1.append(nums[i])
            else:
                result2.append(nums[i])

        return result1 + result2