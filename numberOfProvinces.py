'''
Question: Number of Provinces 
https://leetcode.com/problems/number-of-provinces/
A province is a group of directly or indirectly connected cities (basically a group of connected nodes)
Count number of provinces in the graph.
i.e. 3 disconnected nodes = 3 provinces 
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited, n = set(), len(isConnected)
        def dfs(node): 
            for i in range(n): 
                if i == node: continue 
                if i in visited: continue 
                if isConnected[node][i] == 1: 
                    visited.add(i)
                    dfs(i)
        
        count = 0
        for node in range(n): #n = number of nodes in the graph
            if node in visited: continue 
            visited.add(node) #the node itself will be trivially counted in the for loop outside of dfs
            dfs(node)
            count += 1
        return count
