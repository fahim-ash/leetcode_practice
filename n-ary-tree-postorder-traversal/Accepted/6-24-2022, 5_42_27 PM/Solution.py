// https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        res=[]
        def dfs(root):
            if not root:
                return res
            for child in root.children:
                dfs(child)  
            res.append(root.val)
        
        dfs(root)
        return res
            
            

            
            
            
            
        