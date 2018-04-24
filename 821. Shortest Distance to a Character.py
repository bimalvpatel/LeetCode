'''
https://leetcode.com/problems/shortest-distance-to-a-character/description/

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

'''

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = []
        charpos = [-1]
        for i in range(S.count(C)):
            charpos.append(S.index(C,charpos[-1]+1))
        i = 1
        lofs = len(S)
        lofchar = len(charpos)
        for j in range(lofs):
            dist1 = abs(j-charpos[i])
            if i+1 < lofchar:
                dist2 = abs(j-charpos[i+1])
            else:
                dist2 = 10001
            if dist1 > dist2:
                i += 1
            result.append(min(dist1,dist2))
        return result