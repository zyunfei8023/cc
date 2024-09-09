f = open("shi.txt",encoding="UTF-8")

content = f.read(3)
print(content)

line = f.readline()
print(line)


lines = f.readlines()
print(lines)

f.close()
