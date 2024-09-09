def read_file():
    a=10
    b=0
    
    try:
        rst = a/b 
        print("1.",rst)
        return rst
    except:
        print("2.出现异常")
        
    finally:
        print("3.close")
        
def write_file1():
    file=None
    try:
        file = open("hiahia.txt","w")
        a=10
        b=0
        rst = a/b
        file.write(f"haha:{rst}")
    except Exception as e:
        print("异常",e,type(e))
    finally:
        if file  is not None:
            file.close()
        print("关闭资源")
    
read_file()
write_file1()
        
        