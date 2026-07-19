class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set()
        for i in nums:
            set_num.add(i)
        if(len(set_num)==len(nums)):
            return False
        
        else:
            return True
        


        