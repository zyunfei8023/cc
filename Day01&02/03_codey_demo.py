container= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

password= input ("密码")

for ele in password:
    if ele not in container:
        print("不合法",ele)
        break
else:
    print("合法")