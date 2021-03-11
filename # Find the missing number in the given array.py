def missing_num(a):
    n=a[-1] #To get the last number of array 
    total=n*(n+1)//2 #to calculate the natural number 
    sum1=0
    sum1=sum(a)   #sum of number given number 
    result=total-sum1 #To find missing number in the gievn number
    print(result)
a=[1,2,4,5,6]
missing_num(a)
