from abc import ABC , abstractmethod

class ClassAbstraction(ABC):
    def print(self,x):
        self.x = x
        print("the value of x" , self.x)

    @abstractmethod
    def task(self):
        print("I dont have any ideas on what to type")

    

class test(ClassAbstraction):

    def task(self):
        print("this is a subclass ?")

test_object = test()
test_object.print(5)
test_object.task()


