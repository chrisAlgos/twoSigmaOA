'''
https://leetcode.com/problems/regular-expression-matching/
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        '''
        idea: refer to Tushar Roy's video 
        '''
        
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        
        
        ## handle row 0 in dp and handles col 0 in dp 
        dp[0][0] = True ## "" matches "" 
        
        ## "" matches *, "" matches **, "" doesn't match **x*
        for i in range(1, len(p)+1): 
            if p[i-1] == '*': 
                dp[0][i] = dp[0][i-1]

        # start from the inner
        for i in range(1, len(s)+1): 
            for j in range(1, len(p)+1): 
                if s[i-1] != p[j-1]: # if current char in s doesn't match up with char in p 
                    if p[j-1] =='?': # single character comparison
                        dp[i][j] = dp[i-1][j-1] # if prev s[:i] matches with prev p[:j], we can say the characters match
                    elif p[j-1] == '*': # multi character comparison 
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] # exclude '*' or s[i] (making * a 0 sequence)
                    else: # characters don't match up 
                        dp[i][j] = False 
                else: 
                    dp[i][j] = dp[i-1][j-1] 

        return dp[-1][-1]
