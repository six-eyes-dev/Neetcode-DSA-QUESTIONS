class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_freq.keys())[:k]