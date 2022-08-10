from colorama import Style,Fore,Back
def bmi():
    name = input(Fore.YELLOW + "Enter your name: ")
    cm_or_m = input("""Select: 1. for your Height in meter:  
       2. for your height in centimeter: """)

    if (cm_or_m == '1'):
        height = int(input("Enter your Height in Meter: "))
        height = float(height/100)

    else:
        height = int(input("enter your Height in Centimeter: "))
        height = float(height / 100)

    weight = float(input("Enter your Weight in Kilograms: "))

    cal =( weight/float(height * height))
    print(Fore.GREEN,"Thank you using my BMI calculator")
    print()
    if(cal <= 18.5):
        print(Fore.RED,name,"you are Underweight.",Fore.BLUE,
                   "So Maintaining a healthy weight is important for your heart health and "
                   "Moving more can lower your risk factors for heart disease.")
    elif(cal > 18.5 and cal <= 24.9 ):
        print(Fore.RED,name, "you are normal weight.",Fore.BLUE,
                    "Maintaining a healthy weight is important for your heart health and "
                    "Moving more can lower your risk factors for heart disease.")
    elif(cal >= 25 and cal <=29.9):
        print(Fore.RED,name, "you are over weight.",Fore.BLUE,
                    "So Maintaining a healthy weight is important for your heart health and "
                    "Moving more can lower your risk factors for heart disease.")
    else:
        print(Fore.RED,name, "you are obesity.",Fore.BLUE,
                    "So Maintaining a healthy weight is important for your heart health and "
                    "Moving more can lower your risk factors for heart disease.")

bmi()