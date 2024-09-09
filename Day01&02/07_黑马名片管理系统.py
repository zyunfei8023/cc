tips = """
**************************************************
欢迎使用[名片管理系统]V1.0

1.新建名片
2.显示名片
3.查询名片

0.退出系统
**************************************************"""

cards =[
    ["唐三藏","12121212","31313","2332@qq.com"],
    ["唐二藏","12124444","31314","4422@qq.com"],
    ["唐一藏","12123333","22222","2222@qq.com"]
]
def create_card():
    print("[新建名片]")
    name = input("请输入姓名")
    phone = input("请输入电话号")
    QQnum = input("请输入QQ号码")
    email =input("请输入邮箱")
    card = [name, phone, QQnum, email]
    cards.append(card)
    print("创建完成{}".format(name))

def show_cards():
    print("show cards")
    for card in cards:
        print("{}\t{}\t{} \t{}".format(card[0],card[1],card[2],card[3]))
        


        

def search_cards():
    s_name = input("请输入姓名")
    for card in cards:
        if s_name == card[0]:
            print("找到了->",card)
            handle_card(card)
            break
    else:
        print("查无此人")

def handle_card(card):
    while True:
        action = input("请输入对名片的操作: 1.修改/ 2.删除/ 0.返回上一级:")
        if action == "1":
            print("修改名片")
            card[0]=input("请输入姓名")
            card[1]=input("请输入电话")
            card[2]=input("请输入QQ")
            card[3]=input("请输入邮箱")
            print("修改完成")
            break
        elif action == "2":
            print("删除")
            cards.remove(card)
            print("删除完成")
            break
        elif action == "0":
            print("返回")
        else:
            print("输入错误，重新输入",action)
            

while True:
    print(tips)
    action = int(input("请输入操作数："))
    if action == 1:
        create_card()
    elif action == 2:
        show_cards()
    elif action == 3:
        search_cards()
    elif action == 0:
        print("退出系统")
    else:
        print("输入操作错误，请重新输入")
 