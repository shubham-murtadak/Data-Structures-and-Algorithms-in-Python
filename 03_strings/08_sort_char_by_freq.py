class Solution:
    def frequencySort(self, s: str) -> str:
        #step 1 count
        st={}
        for i in s:
            if i not in st:
                st[i]=1
            else:
                st[i]+=1
        
        # print(st)
        # print(st.items())

        #step 2 sort
        st=sorted(st.items(),key=lambda item:item[1],reverse=True)

        #frame answer
        ans=""
        for i in st:
            ans+=i[0]*i[1]

        return ans



if __name__=='__main__':
    s = Solution()

    st="tree"
    ans=s.frequencySort(st)

    print(ans)