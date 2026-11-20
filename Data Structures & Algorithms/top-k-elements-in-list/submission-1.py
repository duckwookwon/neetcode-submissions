class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        common = {}
        for i in nums:
            common[i] = common.get(i,0)+1
            
        sorted_common = sorted(common, key=common.get, reverse = True)

        return sorted_common[:k]
            
        
