def sum_nums(*args):
    print(args,type(args))
    
    rst = 0
    for i in args:
        rst +=i
    return rst

def sum_nums1(name,*args):
    print(name,type(name))
    print(args,type(args))
    
    rst =0
    for i in args:
        rst +=i
    return rst


print(sum_nums(3,4,5,34))
print(sum_nums1("zzzz",1,2,3,4,5,6))


def keyword_args(aaa,**kwargs):
    print(kwargs, type(kwargs))
    print(kwargs["age"])
    print(kwargs["name"])
    print(aaa)
    
keyword_args(name="黑猴",aaa="haha",age = 500,height=160.2)
    
