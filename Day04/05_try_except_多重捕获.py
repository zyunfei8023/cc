
def write_file():
    file =None
    try:
        file = open("haha.txt", "w")
        a=10
        b=5
        rst = a/b
        arr=[2,3]
        val=arr[0]
        
        file.write(f"haha:{rst}")
    except ZeroDivisionError as e:
        print("除零异常",e,type(e))
    except PermissionError as e:
        print("权限异常",e,type(e))
    except IndexError as e:
        print("索引异常:", e, type(e))
    except Exception as e: # Exception
        print("出现未知异常：", e, type(e)) # 
    finally:
        if file is not None:
            file.close()
        print("关闭资源")
  

write_file()