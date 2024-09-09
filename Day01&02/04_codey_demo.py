def hi_world():
    print("hellow,world")
    print("hellow,world")
    print("hellow,world")


def sum(a,b):
    return a+b

def my_max(a,b):
    return a if a>b else b

def cacl(a,b):
    multiply= a*b
    divide=a/b if b!=0 else None
    return multiply,divide

x, y=cacl(5,6)
print("x:{} y:{}".format(x,y))