def write_file():
    file =None
    try:
        file =open("hahha.txt","w")
        a=10
        b=2
        rst = a/b
        file.write(f"haha:{rst}")
        print("无异常时，执行的代码1")
    except Exception as e :
        print("出现异常：",e,type(e))
    else:
        print("无异常2")
    finally:
        if file is not None:
            file.close()
        print("关闭资源")
    
write_file()