a=int(input("Enter your marks: "))
print ("You Entered a marks:",a)
if a>=90 and a<=100:
    print("A")
if a>=80 and a<=89:
    print("B")
if a>=70 and a<=79:
    print("C")
if a>=60 and a<=69:
    print("D")
if a<60 and a>=0:
    print("F")
if a<0 or a>100:
    print("Invalid range")

