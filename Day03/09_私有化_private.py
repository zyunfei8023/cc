class BankAccount:
    def __init__(self,account_number,balance)-> None:
        self._account_number =account_number
        #属性私有化
        self.__balance=balance
        
    def __str__(self)->str:
        return "账号：{}余额：{}".format(self._account_number,self.__balance)
    
    #方法私有化
    def __pay_charge(self):
        self.__balance-=5
    
    def deposit(self,amouunt):
        self.__balance+=amouunt
        
    def withfraw(self,amount):
        if amount<=0:
            print(f"金额异常：{amount}.取不了")
            return
        if self.__balance<amount:
            print("余额不足")
            return
        
        self.__balance-=amount
        self.__pay_charge()
        
        
account = BankAccount("12313",1000)

account.deposit(200)
account.withfraw(300)

print(account)
