string = "hello"
print(string[1])

print("asdad".isalpha())
print("1231".isnumeric())

print("pop123".startswith("pop12"))
print("pop123".endswith("23"))


print("------------------------------")
print("1wrqrqrqr".index("q"))
print("1wrqrqrqr".find("2"))

print("qwrq.txt.mp4".rfind("."))
print("qwrq.txt.mp4".find("."))
print("asdasdasdadas.csadC".replace("a","A",2))

print("张三葬|王大拿|孙悟空".split("|"))
lis= ['张三葬', '王大拿', '孙悟空']
print("*".join(lis))

print("\t abc \n".strip())
print(" abc ".strip())
print(" abc ".upper())