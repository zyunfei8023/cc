sss = """--------------------------------------------
您输入的字符串: {}
长度: {}
逆序后为: {}
字符统计结果: {}
--------------------------------------------"""

string = ""
while True:
    string=input("请输入字符串")
    if len(string)>=32:
        print("过长")
        continue
    break

stat_dict = dict()

for s in string:
    if s not in stat_dict:
        stat_dict[s]= 1
    else:
        stat_dict[s]+=1
        
stat_str = ["{}->{}".format(k,v) for k,v in stat_dict.items()]

print(" ".join(stat_str))


print(sss.format(string,len(string),string[::-1]," ".join(stat_str)))
