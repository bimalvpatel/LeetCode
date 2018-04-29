class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        cnt = [0]*121
        for i in ages:
            cnt[i]+=1
        '''
        age[B] <= 0.5 * age[A] + 7
        age[B] > age[A]
        age[B] > 100 & & age[A] < 100
        '''
        ans = 0
        for a in range(1,121):
            intercnt = 0
            for b in range(1,a+1):
                if (2*b <= a + 14):
                    continue
                if b > 100 and a < 100:
                    continue
                intercnt += cnt[b]
                if a == b:
                    intercnt -= 1
            ans += intercnt*cnt[a]
        return ans