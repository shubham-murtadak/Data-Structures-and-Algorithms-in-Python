class Solution:
    def maxDepth(self, s: str) -> int:
        
        cnt=0
        maxi=0
        for i in s:
            if i=='(':
                cnt+=1
                maxi=max(cnt,maxi)
            
            elif i==')':
                cnt-=1
        
        return maxi

            







if __name__=='__main__':
    s="(1+(2*3)+((8)/4))+1"

