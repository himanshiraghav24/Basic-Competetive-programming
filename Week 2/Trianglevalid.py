a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))

if (a+b+c == 180):
    if(a>0 and b>0 and c>0):
        print("Trinagle is valid")
else:
    print("Triangle is not valid")