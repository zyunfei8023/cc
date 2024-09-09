def add(x, y):
    """返回 x 和 y 的和"""
    return x + y

def subtract(x, y):
    """返回 x 减去 y 的结果"""
    return x - y

def multiply(x, y):
    """返回 x 和 y 的乘积"""
    return x * y

def divide(x, y):
    """返回 x 除以 y 的结果"""
    if y == 0:
        return "除数不能为零"
    return x / y

def main():
    print("欢迎使用简易计算器！")
    print("请选择操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")

    choice = input("请输入你的选择 (1/2/3/4): ")

    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))

    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, str):
            print(result)
        else:
            print(f"{num1} / {num2} = {result}")
    else:
        print("无效的选择，请输入 1, 2, 3 或 4")

if __name__ == "__main__":
    main()