
# implimenttion of singly linklist with all functions

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None 
    


class Linklist:

    def __init__(self):
        self.head=None 
    
    def insert_at_end(self,value):
        new_node=Node(value)
        if self.head is None :
            self.head=new_node 
        
        else:
            temp=self.head

            while(temp.next):
                temp=temp.next
            
            temp.next=new_node 
    
    def insert_at_head(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node 
        
        else:
            new_node.next=self.head 
            self.head=new_node 

    
    def insert_at_specific_position(self,position,value):
        new_node=Node(value)
        temp=self.head 

        cnt=1 

        while(cnt<position-1):
            temp=temp.next
            cnt+=1
        
        new_node.next=temp.next
        temp.next=new_node

    
    def delete_from_head(self):
        if self.head is None :
            print("linklist is already empty thier is nothing to delete !")
        
        temp=self.head 

        self.head=temp.next
        temp.next=None

        del temp

    
    def delete_from_tail(self):
        if self.head is None:
            print("linklist is already emtpy thier is nothing to delete !")
            return 
        
        temp=self.head 

        if(self.head.next is None):
            self.head=None
            return 

        while(temp.next.next):
            temp=temp.next 
        
        temp.next=None 
        
    
    def delete_from_specific_position(self,pos):
        curr=self.head 
        prev=None 

        if self.head.next is None:
            self.head=None 
            return 

        cnt=1
        while(cnt<pos):
            prev=curr
            curr=curr.next
            cnt+=1
        
        prev.next=curr.next
        curr.next=None 
        del curr

    
    def search(self,val):
        temp=self.head 

        while(temp):
            if temp.value==val:
                return True 
                break
            temp=temp.next
        
        return False 
            

    def print_linklist(self):
        temp=self.head 

        while(temp):
            print(temp.value,end='->')
            temp=temp.next 



if __name__=='__main__':
    ll=Linklist()

    ll.insert_at_end(5)
    ll.insert_at_end(10)
    ll.print_linklist()
    ll.insert_at_head(1)
    print()
    ll.print_linklist()
    print()
    ll.insert_at_specific_position(2,15)
    ll.print_linklist()

    # ll.delete_from_head()
    print()
    ll.print_linklist()
    # ll.delete_from_tail()
    print()
    # ll.print_linklist()
    print()
    ll.delete_from_specific_position(2)
    ll.print_linklist()
    print()
    ans=ll.search(12)
    print(ans)
