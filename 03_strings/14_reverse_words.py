class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.strip()
        print(f"s after removing spaces :",s)

        s=s.split()
        print(f"s after splitting on spaces",s)

        s=s[::-1]
        print(f"s after reversing words :",s)

        s=" ".join(s)
        print(f"s after joinging :",s)







if __name__=='__main__':
    st= "a good   example"
    s=Solution()
    print(s.reverseWords(st))