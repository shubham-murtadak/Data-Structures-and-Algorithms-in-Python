class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        
        else:
        
            dic={}

            ans=True

            n=len(s)

            for i in range(n):
                if s[i] not in dic and t[i] not in dic.values():
                    dic[s[i]]=t[i]
                
                elif  s[i] not in dic and t[i] in dic.values():
                    ans=False
                    break

                else:
                    if dic[s[i]]==t[i]:
                        continue
                    else:
                        ans=False
                        break
            
            return ans


class Solution2:
    def isIsomorphic(self,s:str,t:str)->bool:

        forward_map={}
        backward_map={}
        if len(s)!=len(t):
            return False 
        
        else:
            for i in range(len(s)):
                a,b=s[i],t[i]

                if a in forward_map:
                    if(forward_map[a]!=b):
                        return False 
                        break
                else:
                    if b in backward_map:
                        return False
                        break 
                
                forward_map[a]=b
                backward_map[b]=a
            
            return True


if __name__=='__main__':
    s = "bbbaaaba"
    t = "aaabbbba"


    obj=Solution()
    ans=obj.isIsomorphic(s,t)

    if ans==True:
        print(f"{s} and {t} are isomorphic strings !")
    else:
        print(f"{s} and {t} are not isomorphic stings !")
