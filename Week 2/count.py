a=int(input("Enter a number:"))
if a ==0:
    count=1
else:
    if a <0:
        a=-a
        
    count=0
    while a>0:
        count+=1
        a//=10
print("count of digit",count);
        
    