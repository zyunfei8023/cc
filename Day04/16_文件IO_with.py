content_lst = [
    "🐓哎呦，你干嘛", 
    "🐔只因你太美",
    "🕺两年半练习生"
]


with open("e.txt","w+",encoding="UTF-8") as f:
    

    for line in content_lst:
        f.write(f"{line}\n")
    
print("is closed :",f.close())