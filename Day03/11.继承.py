class Person(object):
    
    def __init__(self,name,age)-> None:
        self.name =name
        self.age =age
        
        
    def say_hello(self):
        print("say hello from",self.name)
        
    def eat(self):
        print(self.name ,"eat")
        
    def __str__(self)->str:
        return "name:{}  age{}".format(self.name ,self.age)
    
class Student(Person):
    def __init__(self,name,age,score)->None:
        super().__init__(name,age)
        
        self.score =score
        
    def play_game(self):
        print(f"{self.name}play game")
        
    def __str__(self)->str:
        return "学生 name:{} age{} score{}".format(self.name,self.age,self.score)
        
        
stu = Student("小吗喽",15,95)
print(stu)
stu.say_hello()
stu.play_game()
