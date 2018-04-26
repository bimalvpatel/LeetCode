class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        lineuse = 0
        for i in S:
            if lineuse + widths[ord(i)-ord('a')] <= 100:
                lineuse += widths[ord(i)-ord('a')]
            else:
                lines += 1
                lineuse = widths[ord(i)-ord('a')]
        return [lines,lineuse]