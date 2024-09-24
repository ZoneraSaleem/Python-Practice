def calculate_bill():
    while True:
     print("\nDiscount System")
     print("Welcome to our Store")
     inamount=int(input(f"\nEnter Total amount: "))
     membership = input("Do you have a membership? ") .lower() == "yes"  # if statement compares the lowercase version of the user’s input to the lowercase string "yes"
     if inamount>= 100 and inamount< 200: # we also write the expression in simple form if 100 <= inamount < 200:
         if membership:
             dis = inamount * 7 / 100
             tb = inamount - dis
             print(f"\nyour Total bill {tb} is")
         else:
             dis = inamount * 2 / 100
             tb = inamount - dis
             print(f"\nyour Total bill {tb} is")
     elif inamount >= 200 and inamount < 300:# we also write the expression in simple form if 200 <= inamount < 300:
         if membership:
           dis = inamount * 10 / 100
           tb = inamount - dis
           print(f"\nyour Total bill {tb} is")
         else:
           dis = inamount * 5 / 100
           tb = inamount - dis
           print(f"\nyour Total bill {tb} is")
     elif inamount >= 300 and inamount < 400: # we also write the expression in simple form if 300 <= inamount < 400:
         if membership:
           dis = inamount * 12 / 100
           tb = inamount - dis
           print(f"\nyour Total bill {tb} is")
         else:
           dis = inamount * 8 / 100
           tb = inamount - dis
           print(f"\nyour Total bill {tb} is")
     elif inamount >=500:
        if membership:
            dis = inamount * 20 / 100
            tb = inamount - dis
            print(f"\nyour Total bill {tb} is")
        else:
            dis = inamount * 15 / 100
            tb = inamount - dis
            print(f"\nyour Total bill {tb} is")
            break

calculate_bill()