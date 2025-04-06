

# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None




class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        
        new_node=Node(x)
        
        if head is None:
            head=new_node
        
        else:
        
            temp=head 
            
            while(temp.next):
                temp=temp.next 
            
            temp.next=new_node
            
        
        return head
