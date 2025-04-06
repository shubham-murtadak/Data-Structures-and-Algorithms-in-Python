class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if (len(s)!=len(goal)):
            return False 
        
        for i in range(len(s)):
            print(f"{s[0]}->{goal[i]}")
            if(s[i]==goal[0]):
                if s[i:]+s[:i]==goal:
                    print(f"{s[i:]}+{s[:i]}=={goal}")
                    return True
        
        return False



if __name__=='__main__':
    # s = "abcde"
    # goal = "cdeab"

    # s = "abcde"
    # goal = "abced"

    s="abcde"
    goal ="abced"

    sol=Solution()
    ans=sol.rotateString(s,goal)
    print(ans)