ages = {
    "tom":18,
    "tim":17,
    "tlm":16,
    "ttm":15,
}

#增
ages["zha"]=22
ages.setdefault("addasd",23)

#删
ages.pop("addasd")
del ages["zha"]

#改
ages["ttm"]=22

#查询
print(ages["ttm"])
print("ttm" in ages)

print(ages,type(ages))
print("-----------------")

#遍历
for key in ages:
    print(key,ages[key])
print("--------------------------------")
for key in ages.keys():
    print(key,ages[key])

print("3-----------------------------------")

for value in ages.values():
    print(value)

print("4-----------")

for item in ages.items():
    print(item,type(item))

for (key,val) in ages.items():
    print(key,val)
    
aaa =dict()
print(aaa,type(aaa))
bbb=set()
print(bbb,type(bbb))
    