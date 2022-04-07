class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        if len(stones) == 1:
            return 1
        if len(stones) == 0:
            return 0
        if len(stones) == 2:
            stones.sort()
            return stones[-1] - stones[-2]
        if len(stones) > 2:

            while len(stones) > 2:
                stones.sort()
                x,y = stones[-1],stones[-2]
                if x == y:
                    stones.pop(-1)
                    stones.pop(-1)

                else:
                    x = abs(x-y)
                    stones.pop(-1)
                    stones[-1] = x 
                
                if len(stones) == 2:
                    return abs(stones[-1] - stones[-2])
                else:
                    continue

            if len(stones):
                return stones[-1]

        if len(stones):
            return stones[-1]

obj  = Solution()
print(obj.lastStoneWeight([10,4,2,10]))