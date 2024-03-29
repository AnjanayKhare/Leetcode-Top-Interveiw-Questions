class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #done by 2-pointer
        fr = {fruits[0]:1}
        ans = 1
        i = 0
        j = 1
        n = len(fruits)
        while i<=j and j<n:
            if len(fr) <2:
                fr[fruits[j]] = fr.get(fruits[j], 0) + 1
                j+=1
            else:
                if fruits[j] in fr:
                    fr[fruits[j]] = fr.get(fruits[j], 0) + 1
                    j+=1
                else:
                    fr[fruits[i]] -= 1
                    if fr[fruits[i]] == 0:
                        del fr[fruits[i]]
                    i+=1
            ans = max(ans, sum(fr.values()))
        return ans
