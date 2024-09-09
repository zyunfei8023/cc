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


a = Person("桑尼", 16)    

#print(p)

print(a.name)
print(a.age)
print(a.version)

a.eat()
a.run()
a.say_hellow("小兰")

p2 =Person("小红",13)

print(p2.name)
print(p2.age)
