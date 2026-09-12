class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[]
        for num in range(left,right+1):
            temp=num
            valid=True

            while(temp>0):
                rem=temp%10
                temp//=10

                if rem==0:
                    valid=False
                    break

                if num%rem!=0:
                    valid=False
                    break
            if valid:
                result.append(num)
        return result                         

      