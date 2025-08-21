a=int(input("Enter a number:"))

if(a<=25):
    print("Grade D")
elif(a>=25 and a <= 45):
    print("Grade C")
elif(a>=45 and a <=65):
    print("Grade B")
elif(a>=65 and a <=85):
    print("Grade A")
elif(a>=85):
    print("Grade A+")
else:
    print("Fail")

