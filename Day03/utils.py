name = "张三外挂!"

#定义函数

def add(a,b):
    return a+b

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"姓名: {self.name} 年龄:{self.age}"
    
    


if __name__ == "__main__":
    print("软件名:",name)
    print("正常运行")
    print(add(3,5))

