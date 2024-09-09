import os

while True:
    file_name = input("请输入要备份的文件名:")
    # 首先判断文件是否存在，存在，则结束循环
    if os.path.exists(file_name):
        break
    
    # 文件不存在
    print("文件不存在：", file_name)
    
print("开始拷贝:",file_name)

dot_index = file_name.rfind(".")
filename_prefix = file_name[:dot_index]

filename_suffix = file_name[dot_index:]

new_file_name = f"{filename_prefix}[复制]{filename_suffix}"

print(new_file_name)

with open(file_name,"rb") as f:
    content = f.read()
    print(type(content),len(content))
    
    with open(new_file_name,"wb") as new_file:
        new_file.write(content)
        print("复制完成")