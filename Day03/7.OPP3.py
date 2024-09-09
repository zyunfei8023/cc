class Person:
   
    def __init__ (self ,name ,age):
        
        self.name=name
        self.age=age
        self.version =1.0
        
        
    def eat(self):
        print(self.name,"吃")
    
    def run(self):
        print(self.name,"跑")
        
    def say_hellow(self,target):
        print("hello: ",target)
    
    def __str__ (self):
        return f"姓名:{self.name} 年龄:{self.age}"
    
p2=Person("小红",13)
print(p2)

p= Person("桑尼",16)
print(p)
p.say_hellow(p2.name)
    
    
