content_lst = [
    "哎呦，你干嘛", 
    "只因你太美",
    "两年半练习生"
]

file = open ("c.txt","w+",encoding="UTF-8")

for line in content_lst:
    file.write(line + "\n")
    
file.close()