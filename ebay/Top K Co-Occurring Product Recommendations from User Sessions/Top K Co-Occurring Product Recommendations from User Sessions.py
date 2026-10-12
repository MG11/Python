class Solution:
    def topKCoOccurring(self, sessions, target, k):
        # Write your code here
        pass
        counter = {}
        for session in sessions:
            if target not in session:
                continue
            
            for product in session:
                counter[product] = counter.get(product, 0) + 1
        
        entries = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

        ans = []
        
        for product, _ in entries:
            if len(ans) >= k:
                break
            ans.append(product)
        
        return ans
