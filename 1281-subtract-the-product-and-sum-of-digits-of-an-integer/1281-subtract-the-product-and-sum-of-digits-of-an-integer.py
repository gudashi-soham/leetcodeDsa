class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        productofdigits=1
        sumofdigits=0
        rem=0


        while (n>0):
            rem=n%10
            productofdigits*=rem
            sumofdigits+=rem
            n//=10
        return productofdigits- sumofdigits    
