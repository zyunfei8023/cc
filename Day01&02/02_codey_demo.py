for i in range(100,1000):
    hundred =i//100
    ten =i//10%10
    digit = i%10
    if(hundred**3+ten**3+digit**3)==i:
        print(i)