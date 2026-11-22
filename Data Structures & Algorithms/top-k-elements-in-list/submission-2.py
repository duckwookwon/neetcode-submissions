from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_num = Counter(nums)
        return [x for x,y in new_num.most_common(k)]