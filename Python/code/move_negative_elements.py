class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        m = set(a)
        k = set(b)
        m = m.union(k)
        return len(list(m))
        
        #code here
