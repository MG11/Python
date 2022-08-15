class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = {}
        for i in s:
            if my_dict.get(i, None):
                my_dict[i] +=1
            else:
                my_dict[i] = 1
        
        my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        
        ans = ""
        for k in my_dict:
            ans += k[0]*k[1]
        
        return ans
        