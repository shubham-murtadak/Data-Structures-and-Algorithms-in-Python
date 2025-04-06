 
class Myclass:

    def __init__(self,name):
        self.name=name 
    
    def greet(self):
        print(f"hello {self.name}")


class Childclass(Myclass):
    def __init__(self,name):
        super().__init__(name)



if __name__=='__main__':
    obj=Childclass("shubham")
    obj.greet()