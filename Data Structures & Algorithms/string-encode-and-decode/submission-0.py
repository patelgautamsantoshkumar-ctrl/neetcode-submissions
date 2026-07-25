class Solution:

    def encode(self, strs: List[str]) -> str:
        strz = list()
        counter =0
        for i in strs:
            strz.insert(counter,str(len(i)))
            counter +=1
            strz.insert(counter,"#")
            counter +=1
            strz.insert(counter,i)
            counter +=1
        print(strz)
        return "".join(strz)


    def decode(self, s: str) -> List[str]:
        arry = list()
        i=0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            arry.append(s[i:j])
            i = j
        return arry
