

class Node:
    def __init__(self,value,next=None):
        self.next=next
        self.value=value


class Linklist:

    def __init__(self):
        self.head=None
    
    def insert(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node

        else:
            current=self.head 

            while current.next:
                current=current.next 
                self.head=current 

        return self.head

if __name__=='__main__':
    obj=Linklist(5)

    print(obj.head)
