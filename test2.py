
def fibonnaci(n):

    if(n==0):
        return 0 
    if(n==1):
        return 1 
    
    return fibonnaci(n-1)+fibonnaci(n-2)



def factorial(n):

    if(n==0):
        return 1 
    
    return n*factorial(n-1)




    
       
        



if __name__=='__main__':
    ans=factorial(4)
    print(ans)