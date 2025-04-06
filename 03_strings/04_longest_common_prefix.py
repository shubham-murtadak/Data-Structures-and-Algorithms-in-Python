

def longest_common_prefix(st:list)->str:
    
    st.sort()

    start=st[0]
    end=st[-1]

    n=len(start)

    print("start is :",start)
    print("End is :",end)
    print("n is :",n)

    ans=""

    for i in range(0,n):
        if(start[i]==end[i]):
            print(f"start i is {start[i]} end i is :{end[i]}")
            ans=ans+start[i]
        else :
            return ans 
    
    return ans



if __name__=='__main__':
    # st=["flower","flow","flowight"]
    st=["dog","racecar","car"]

    # start=st[0]
    # end=st[-1]

    ans=longest_common_prefix(st)


    print("ans is :",ans)