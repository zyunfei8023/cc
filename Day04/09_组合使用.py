def milk_tea_shop(kind,*argumennts,**keywords):
    print(f">> 老板，给我来杯: {kind} !")
    print(f">> 对不起: 我的 {kind} 卖完了 !")
    for index,arg in enumerate(argumennts):
        print(f"{index + 1} : {arg}")
        
    print("-"*50)
    for key in keywords:
        print(f"{key} - >{keywords[key]}")
        

milk_tea_shop(
    "QQ 乃氖好喝到爆的买普茶",
    "微冰", "少糖", "加黑珍珠", # 写多个
    addr="创维创新谷2#B栋5楼", phone="13688886666", name="狗剩"
)
    
    