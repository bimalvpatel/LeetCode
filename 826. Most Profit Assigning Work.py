class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        temp = {}
        for i in range(len(difficulty)):
            temp[difficulty[i]] = max(profit[i],temp.get(difficulty[i],-1))
        profit = 0
        dp = []
        difficultysorted = sorted(difficulty)
        maxp = 0
        for c in range(max(difficultysorted)+1):
            maxp = max(maxp,temp.get(c,-1))
            dp.append(maxp)
        #print(dp)
        for w in range(len(worker)):
           #print(dp[worker[w]])
           if worker[w] > len(dp)-1:
               p = dp[-1]
           else:
               p = dp[worker[w]]
           #print(p)
           profit = profit + p
        return profit

'''
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
'''