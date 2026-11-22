from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        container = defaultdict(list)
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char) - ord('a')] +=1
            count_new =tuple(count)
            container[count_new].append(s)
        return list(container.values())
        
