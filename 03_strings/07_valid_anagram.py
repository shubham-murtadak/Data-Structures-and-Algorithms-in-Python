class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst=[0]*26
        lst2=[0]*26

        for i in s:
            lst[ord(i)-ord('a')]+=1
        
        for j in t:
            lst2[ord(j)-ord('a')]+=1

        
        return lst==lst2
    
    #sol2:
    # lst=sorted(list(s))
    # lst2=sorted(list(t))

    # print(lst==lst2)

    #sol3 : from collecitons import Counter 
    # return Counter(s)==Counter(t)





if __name__=='__main__':
    solution = Solution()
    s = "asm"
    t = "mas"
  
    # print(Counter(t))

    # ans=solution.isAnagram(s,t)
    # print(ans)

