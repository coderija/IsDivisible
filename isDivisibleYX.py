def is_divisible(n,x,y):
    #your code here
    #n = int(input("enter a number: "))
    if n % x == 0 and n % y==0 :
        return True
            #print ('n=', n,', x= ',x,', y=',y,'=> True becausue',n,'is divisible by ',x, 'and', y)
    elif n % x == 0 and n % y !=0 :
        return False
        #print('n=', n,', x= ',x,', y=',y,'=> False becausue',n,'is not divisible by ',y)
    elif n % x != 0 and n % y ==0 :
        return False
        
        #print('n=', n,', x= ',x,', y=',y,'=> False becausue',n,'is not divisible by ',x)
    else:
        return False
        #print('n=', n,', x= ',x,', y=',y,'=> False becausue',n,'is neither divisible by ',x, 'nor', y)

print (is_divisible(12,7,5))

    
