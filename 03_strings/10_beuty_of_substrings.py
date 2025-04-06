from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:

        n=len(s)
        ans=0
        for i in range(n):
            for j in range(i,n):
                if i!=j:
                    cnt=Counter(s[i:j+1])
                    freq=cnt.values()
                    ans+=max(freq)-min(freq)
                   
            # print(" ")

        return ans 




if __name__=='__main__':
    s = "aabcb"
    sn=Solution()
    ans=sn.beautySum(s)
    print(ans)