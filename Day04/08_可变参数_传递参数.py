score = [83,92,100,95,67,76]

def average(*args):
    print(args,type(args))
    rst =0 
    for i in args:
        rst+=i
    return rst / len(args)

print(average(3,5,7,9))
print(average(*score))

print(*score)

print(83,92,100,95,67,76)

def show_into(**kwargs):
    print(kwargs,type(kwargs))

stu ={
    "name":"Tom",
    "age":23,
    "score":90,
}

show_into(name = "abc",age = 12)
show_into(**stu)
