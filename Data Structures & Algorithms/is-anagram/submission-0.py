class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dis1 ={}
        dis2={}
        for letter in s:
            if letter  not in dis1:
                dis1[letter] = 1
            else:
                dis1[letter] +=1
        for letter in t:
            if letter  not in dis2:
                dis2[letter] = 1
            else:
                dis2[letter] += 1
        
        if dis1 == dis2:
            return True
        else:
            return False






        