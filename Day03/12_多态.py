class Human:
    def eat(self):
        print("人类吃饭")
        
class ZhHuman(Human):
    def eat(self):
        print("中国人用筷子吃饭")
# 美国人
class USAHuman(Human):
    
    def eat(self):
        print("美国人用刀叉吃饭")
        
# 非洲人
class AfricaHuman(Human):
    
    def eat(self):
        print("非洲人用手抓饭（恩希玛）")
def someone_eat(someone: Human):
     
    someone.eat()
    print(type(someone))
     

老张 = ZhHuman()
杰克 = USAHuman()
非哥 = AfricaHuman()

someone_eat(老张)
someone_eat(杰克)
someone_eat(非哥)
