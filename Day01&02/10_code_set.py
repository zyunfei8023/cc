sss = { "孙悟空", "猪八戒", "唐三藏", "猪八戒" ,"沙悟净" }


for item in sss:
    print(item)

sss.add("白骨精")

sss.add("孙悟空")

sss.remove("猪八戒")


sss.discard("niu")
sss.pop()

sss.clear()



print(sss,type(sss))