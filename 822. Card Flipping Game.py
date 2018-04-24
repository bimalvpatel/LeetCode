class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        result = 9999
        same = {x for i,x in enumerate(fronts) if x == backs[i]}
        for x in itertools.chain(fronts, backs):
        #print(x)
            if x not in same:
                result = min(result, x)
            #print("result" + str(result))
        return result % 9999