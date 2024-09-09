name_list = ["流川枫", "佐助", "纲手", "路飞", "柯南", "路飞"]


print(name_list[2])
print(name_list.index("路飞"))
name_list.append("xx")
name_list.remove("xx")
print(name_list.pop(0))
name_list[4]="zzz"
for name in name_list:
    print(name)
    
arg_list =[1,12,4,5]
arg_list.reverse()
arg_list.sort()