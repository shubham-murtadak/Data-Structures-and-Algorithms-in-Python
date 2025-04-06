

#1.
# for  col in range (1,6):
#     for row in range(1,6):
#         print("*",end=" ")
#     print()

# 2.

# row=5
# col=5

# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# 3.

# row=5

# for i in range(0,row+1):
#     for col in range(1,i+1):
#         print(col,end=" ")
#     print()


# 4.
# row=5

# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# 5.

# row=5

# for i in range(0,row):
#     for j in range(row-i):
#         print("*",end=" ")
#     print()


#6. 
# row =5 

# for i in range(0,row):
#     for j in range(row-i):
#         print(j+1,end=" ")
#     print()

# 7. 

# row=5 

def pattern_7(row=5):
    for i in range(0,row):
        for space in range (row-i-1):
            print(" ",end=" ")
        for start in range(2*i+1):
            print("*",end=" ")
        print()

#8.
def pattern_8(row=5):
    for i in range(0,row):
        space_val=i
        for space in range(i):
            print(" ",end=" ")
        
        star_val=(2*row)-(2*i+1)
        for star in range(star_val):
            print("*",end=" ")
        
        print()

# pattern_7()
# pattern_8()

#9.
def pattern_9(row=5):

    for i in range(1,row+1):
        for j in range(i):
            print("*",end=" ")
        print()

    for i in range(1,row):
        for j in range(i,row):
            print("*",end=" ")
        print()


# pattern_9() 

def pattern_10(row=5):
    for i in range(1,row+1):
        for j in range(1,i+1):
            if(i%2==0):
                print("1",end=" ") if j%2==0 else print("0",end=" ")
            else:
                print("0",end=" ") if j%2==0 else print("1",end=" ")

        print()

# pattern_10()

# 11 

def pattern_11(row=4):
    for col in range(1,row+1):
        for star1 in range(1,col+1):
            print(star1,end=" ")

        for space in range(1,((2*row)-(2*col-2))):
            print(" ",end=" ")
        
        for star2 in range(1,col+1):
            print(col-star2+1,end=" ")
        print()

# pattern_11()

def pattern_12(row=5):
    cnt=1
    for col in range(1,row+1):
        for row in range(1,col+1):
            print(cnt,end=" ")
            cnt+=1
        print()

# pattern_12()

# print(ord('A'))
# print(chr(ord('A')))

def pattern_14(row=5):

    for col in range(1,row+1):

        for row in range(1,col+1):
            print(chr(64+row),end=" ")
        print()

# pattern_14()

def pattern_15(row=5):
    for col in range(1,row+1):
        for j in range(1,row-col+2):
            print(chr(64+j),end=" ")
        print()

# pattern_15()

def pattern_16(row=5):
    
    for col in range(1,row+1):
        for row in range(1,col+1):
            print(chr(64+col),end=" ")
        print()

# pattern_16()

#* question
def pattern_17(row=5):
    for col in range(1,row):

        for space in range(1,(row-col+1)):
            print(" ",end="")
        
        for char in range(1,col+1):
            print(chr(64+char),end='')

        for char2 in range(1,col):
            print(chr(64+(col-char2)),end="")
            
        print()


# pattern_17()

def pattern_18(row=5):

    for col in range(1,row+1):
        for j in range(1,col+1):
            print(chr(64+(row-col+j)),end=" ")
        print()

# pattern_18()

def pattern_19_a(row=5):

    for col in range(1,row+1):
        for j in range(1,row-col+2):
            print("*",end=" ")
        
        for space in range(0,(2*col-2)):
            print(" ",end=" ")
        
        for star2 in range(1,(row-col)+2):
            print("*",end=" ")

        print()

def pattern_19_b(row=5):
    for col in range(1,row+1):

        for star1 in range(1,col+1):
            print("*",end=" ")
        
        for space in range(0,((2*row)-2*col)):
            print(" ",end=" ")

        for star2 in range(1,col+1):
            print("*",end=" ")
        print()


# pattern_19_a()
# pattern_19_b()

def pattern_20(row=5):

    for ra in range(1,2*row):

        #star 
        if(ra>row):
            space=((ra-row)*2)+1
            star_cnt=row-(ra-row)+1
        else:
            space=((2*row)-2*ra)+1
            star_cnt=ra+1
        

        #star
        for star1 in range(1,star_cnt):
            print("*",end=" ")

        #spaces
        for space in range(1,space):
            print(" ",end=" ")

        #star
        for star2 in range(1,star_cnt):
            print("*",end=" ")


        print()

        
# pattern_20()

def pattern_21(tot_row=10):

    for row in range(1,tot_row+1):

        if row==1 or row==tot_row:
            star_cnt=int((tot_row/2)+1)
            space=0
        else:
            star_cnt=int((tot_row/tot_row)+1)
            space=tot_row-star_cnt+1
            
        for star1 in range(1,star_cnt):
            print("*",end=" ")
        
        for sp in range(1,space):
            print(" ",end=" ")
        
        for star2 in range(1,star_cnt):
            print("*",end=" ")
        
        print()

            
        



# pattern_21()

def pattern_22(n=4):

    for i in range(0,2*n-1):
        for j in range(0,2*n-1):

            left=j
            top=i
            right=(2*n)-2-j
            bottom=(2*n)-2-i

            print(n-(min(min(left,right),min(top,bottom))),end=" ")

        print()

# pattern_22()

def pattern_23(row=5):
    s=0
    for i in range(1,row+1):
        print(i,end=" ")
        ad=4
        st=i


        for j in range(s):
            st+=ad
            print(st,end=" ")
            ad-=1
        s+=1
        print()


    

# pattern_23()

def pattern_24(n=5):

    for i in range(n):

        for j in range(i+1):
            x=0
            for k in range(j):
                x=x+n-k

            if(j%2==0):
                print(x+i-j+1,end=" ")
            else:
                print(x+n-i,end=" ")

        print()

   

# pattern_24()

arr=[1,2,3,4,5,6,7]

arr[3:]=reversed(arr[3:])

print(arr)




