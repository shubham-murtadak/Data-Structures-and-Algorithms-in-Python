class Solution:
    def romanToInt(self, st: str) -> int:
        n=len(st)

        ans=0
        i=0
        
        map_tab={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        while(i<n):
            if(i+1<n and map_tab[st[i]]<map_tab[st[i+1]]):
                ans-=map_tab[st[i]]
                i+=1
            
            else:
                ans+=map_tab[st[i]]
                i+=1
        
        return ans



if __name__=='__main__':
    st="MCMXCIV"
    

    s=Solution()
    ans=s.romanToInt(st)
    print(ans)