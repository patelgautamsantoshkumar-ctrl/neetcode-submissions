class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dis1 = {}
        count = 0
        
        for i in nums:
            if i in dis1 and (i +i) == target and dis1[i]!=count:
                return [dis1[i],count]
            dis1[i] = count
            
            x = target - i
            if dis1.get(x) is not None and i != x:
                return [dis1[x], dis1[i]]
            
            count += 1



        