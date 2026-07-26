class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has = {}
        has2 = {}
        counter = 0
        res = []
        counter2 = len(nums)-1


        for i in nums:
            if( counter == 0):
                has[counter] = i
                has2[counter] = nums[counter2]
            else:
                has[counter] = has[counter-1]* i
                has2[counter] = has2[counter-1]* nums[counter2]
            counter += 1
            counter2 -= 1

    
        counter1 = -1
        counter2 = len(nums) - 2
        for i in range(len(nums)):

            if(i == 0):
                res.append(has2[len(nums)-2])
            elif(i == len(nums)-1):
                res.append(has[len(nums)-2])
            else:
                res.append(has2[counter2]* has[counter1])

            counter1 += 1
            counter2 -= 1


        return res




        