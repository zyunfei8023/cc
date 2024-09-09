let =[ele for ele in range(10)]
lst =[ele for ele in range(10) if ele % 2 == 0]

lst =[ele**2 for ele in range(10) if ele % 2 == 0]
print(let)

print(lst)

tup = (ele **2 for ele in range(2,15) if ele % 2 ==1)
print (tuple(tup))


ss={ele ** 2 for ele in range(2,15) if ele %2==1}
print(ss)

_dict ={key:str(key**2) for key in range(1,11) if key %2 == 1}
print (_dict,type(_dict))

lst1 = ["张三", "李四", "王五"]
lst2 = [13, 14, 15, 224, 41, 12]

print (list(zip(lst1,lst2)))

_dict ={ k:v for k , v in zip (lst1,lst2)}
print(_dict)

lst3 = [" 张三  ", " 李四  ", "    王五  "]
lst = [name.strip() for name in lst3]