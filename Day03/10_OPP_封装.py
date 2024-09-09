class WashMachine:
    def __init__(self,brand,capacity)->None:
        self.brand =brand
        self.capacity =capacity
        
        self.__is_closed = False
        self.__mode =0
        self.__motor_speed = 0
        
    def __set_motor_speed(self,speed):
        self.__motor_speed =speed
        
        
    def open_door(self):
        self.__is_closed = False
        print("打开洗衣机")
        
    def close_door(self):
        self.__is_closed= True
        print("关闭洗衣机")
        
    def set_mode(self,new_mode):
        if new_mode in [0,1,2]:
            self.__mode = new_mode
            print("设置模式",new_mode)
        else:
            print("模式无法设置",new_mode)
            
    def wash(self):
        if not self.__is_closed:
            print("please close the door")
            return
        if self.__mode ==0:
            print("ste mode")
            return
        print("放水")
        
        if self.__mode == 1:
            print("轻柔模式")
            self.__set_motor_speed(1000)
            print("马达转速",self.__motor_speed)
            print("开始洗衣服")
        
        elif self.__mode ==2:
            print("狂暴模式，洗大衣")
            
            self.__set_motor_speed(2000)
            print("马达转速",self.__motor_speed)
            print("开始洗衣服")
            
        print("over ")
        
machine = WashMachine("海尔",10)
machine.open_door()

machine.close_door()

machine.set_mode(1)
machine.wash()

        