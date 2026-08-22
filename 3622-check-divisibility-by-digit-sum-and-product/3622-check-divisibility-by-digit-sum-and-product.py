class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp=n
        rem=0
        product=1
        sum=0
        while (temp>0):
            rem=temp%10
            sum+=rem
            product*=rem
            temp//=10
        if n%(product+sum)==0:
            return True 
        else:
            return False        
        