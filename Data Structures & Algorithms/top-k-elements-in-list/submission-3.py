class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dis = {}
        arry = []
        for num in nums:
            if num not in Dis:
                Dis[num] = 1
            else:
               Dis[num] += 1 

        sorted_keys = sorted(Dis, key=Dis.get, reverse=True)
       
        arry = sorted_keys[:k]
        return arry
