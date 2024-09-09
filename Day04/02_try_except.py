a=10
b=0


try:
    rst = a/b   #ZeroDivisionError: division by zero
    print("1-------")
except ZeroDivisionError as e: 
    print("2-----")
    
print("3---------")