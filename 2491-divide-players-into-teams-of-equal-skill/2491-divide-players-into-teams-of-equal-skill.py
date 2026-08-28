class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()

        n=len(skill)
        target=skill[0]+skill[-1]

        total=0
        left=0
        right=n-1
        while left<right:
            if skill[left]+skill[right]!=target:
                return -1
            else:
                total+=skill[left]*skill[right]
                left+=1
                right-=1
        return total        



       
