i = int(input("Enter the number :"))
num=i
result =0
n=len(str(i))
while(i!=0):
    digit=i%10
    result+=digit**n
    i=i//10
if num==result:
    print(+num , "  : Is a Amastrong number")
else:
    print( +num , " : Is not a Amastrong number")