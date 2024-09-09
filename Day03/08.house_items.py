class Item:
        
    def __init__ (self ,name,area)->None:
        self.name=name
        self.area=area
        
    def __str__(self)->str:
        return "str家具:{}占用面积:{}".format(self.name,self.area)
    
    def __repr__(self)->str:
        return "repr家具:{}占用面积:{}".format(self.name,self.area)


 
class House:
    def __init__(self,address,area)->None:
        self.address=address
        self.area=area
        self.free_area=self.area
        self.items=[]
        
    def __str__(self) ->str:
        return f"房子地址:{self.address} 总面积:{self.area} 剩余面积:{self.free_area}"
    def add_item(self,item:Item):
        if self.free_area>=item.area:
            self.items.append(item)
            self.free_area-=item.area
            print("添加成功",item)
        else:
            print("添加失败",item)
            

sofa=Item("沙发",5)
bed  = Item("大床", 15)
desktop = Item("桌椅套装", 30)
home_movie = Item("家庭影院", 60)
print(sofa)
print(bed)
print(desktop)
print(home_movie)


house=House("壹号公寓",100)
print(house)

house.add_item(sofa)
house.add_item(bed)
house.add_item(home_movie)
house.add_item(desktop)
print(house.items)


print(house)
        