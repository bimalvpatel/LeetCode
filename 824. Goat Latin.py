class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        arrs = S.split()
        result = []
        s = "aeiouAEIOU"
        for i in range(len(arrs)):
            if arrs[i][0] in s:
                w = str(arrs[i]) + "ma"
            else:
                w = str(arrs[i][1:]) + str(arrs[i][0]) + "ma"
            w = w + "a" * (i + 1)
            result.append(w)
        return " ".join(result)
