class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        result = ''
        paragraph = paragraph.lower()
        paragraphstr = ''.join([x for x in paragraph if (ord('a') <= ord(x) <= ord('z')) or (x == ' ')])
        paraarr = paragraphstr.split()
        maxoccurance = 0
        tempdict = {}
        for i in range(len(paraarr)):
            if paraarr[i] in tempdict:
                tempdict[paraarr[i]] += 1
            else:
                tempdict[paraarr[i]] = 1
        for k in tempdict:
            if maxoccurance < tempdict[k] and k not in banned:
                result = k
                maxoccurance = tempdict[k]
        return result