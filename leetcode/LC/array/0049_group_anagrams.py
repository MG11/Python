class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)

        for word in strs:
            wordList = [0]*26
            for w in word:
                wordList[ord(w) - 97] += 1
            key = "#".join(str(wordList))
            data[key].append(word)
        
        return list(data.values())
