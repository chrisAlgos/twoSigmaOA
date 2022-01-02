class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(reverse = True, key = lambda x: len(x))
        def helper(a,b):
            #if len(a) == 1:
                #return b[0] == a or b[1] == a
            j = i = 0
            while i < len(a):
                if a[i] != b[j]:
                    if j != i:
                        return False
                    j += 1
                else:
                    j += 1
                    i += 1
            return True
            
        dp = [1 for _ in range(len(words))]
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) == len(words[j]):
                    continue
                if len(words[i]) - 1 > len(words[j]):
                    break
                if helper(words[j], words[i]):
                    dp[j] = max(dp[i] + 1, dp[j])
        return max(dp)
