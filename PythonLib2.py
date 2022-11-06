class Common():
    def Subfields():
        print('Sub-fields in AI are:')
        field=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for temp in field:
            print (temp)
        return
    
    def OddEven():
        a = int(input("Enter a number:"))
        if ((a%2)==0):
            print("{} is a Even number".format(a))
        else:
            print("{} is a odd number".format(a))
        return

    def Eligible():
        b = input("Your Gender:")
        c = int(input("Your Age:"))
        if (b.upper() == 'MALE'and c>=21 ):
            print("ELIGIBLE")
        elif (b.upper() == 'FEMALE' and c>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
        return

    def percentage():
        S1 = int(input("Subject1= "))
        S2 = int(input("Subject2= "))
        S3 = int(input("Subject3= "))
        S4 = int(input("Subject4= "))
        S5 = int(input("Subject5= "))
        Total = S1 + S2 + S3 + S4 + S5
        print("Total : ",Total)
        Percentage = (Total/500)*100
        print("Percentage :",Percentage)
        return

    def triangle():
        h1 = int(input("Height:"))
        b1 = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        A1 = (h1 * b1)/2
        print("Area of Triangle:", A1)
        H1 = int(input("Height1:"))
        H2 = int(input("Height2:"))
        B1 = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        A2 = H1 + H2 + B1
        print("Perimeter of Triangle:", A2)
        return