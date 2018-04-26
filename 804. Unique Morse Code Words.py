class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = set()
        a = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for w in words:
            transtr = ''
            for c in w:
                transtr += a[ord(c)-ord('a')]
            s.add(transtr)
        return len(s)