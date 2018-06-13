My:

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for jewel in J:
            count += S.count(jewel)     
        return count
        
Fastest Code Sample:

class Solution:
    def numJewelsInStones(self, J, S):
        jewelCounter = 0

        for stone in S:
            if stone in J:
                jewelCounter = jewelCounter + 1

        return jewelCounter