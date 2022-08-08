from colorama import Fore, Back, Style
from datetime import date
#git trail
today = date.today()
today = str(today)

today_date = int(today[8:])
today_month = int(today[5:7])
today_year = int(today[:4])
name = input("enter your name: ")
dob = input("enter your dob: ")
birth_date = int(dob[:2])
birth_month = int(dob[3:5])
birth_year = int(dob[6:])

month_count = 0
birth_month1 = birth_month
birth_month2 = birth_month
if(birth_month1 < today_month):
    while(birth_month1 < today_month):
        month_count += 1
        birth_month1 += 1

elif(birth_month > today_month):
     while (birth_month2 != today_month):
        month_count += 1
        if (birth_month2 == 12):
          birth_month2 = 0
        birth_month2 += 1
     today_year -= 1

month_count = str(month_count)
year_count = str(today_year - birth_year)
today_date = str(today_date )
print(Fore.RED+name,"you are :")
print( year_count + " year and " + month_count +" month  and " + today_date + " days old")
today_date = int(today_date)
def leap_fun(x):
    if (((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0)):
        return True
    else:
        return False

leap_year_count = 0
for x in range(birth_year + 1,today_year):
    a = leap_fun(x)
    if(a is True):
        leap_year_count += 1

birth_year_is_leap_year = leap_fun(birth_year)
today_year_is_leap_year = leap_fun(today_year)


def birth_and_today_year_days_cal(input1,input2):
    no_of_days_in_month = 0
    if(input1 <= 12 and input2 != 0):
        for x in range(input1,input2):
            if x in [1, 3, 5, 7, 8, 10, 11]:
                no_of_days_in_month = no_of_days_in_month + 31

            elif (x == 2):
                if (birth_year_is_leap_year is True):
                    no_of_days_in_month = no_of_days_in_month + 29


                else:
                    no_of_days_in_month = no_of_days_in_month + 28


            else:
                no_of_days_in_month = no_of_days_in_month + 30

    return no_of_days_in_month

m1=birth_and_today_year_days_cal(birth_month+1,13)
m2=birth_and_today_year_days_cal(1,today_month)

m3=birth_and_today_year_days_cal(birth_month,birth_month+1)

if(m3 == 31):
    n1 = 31 - birth_date
elif(m3 == 30):
    n1 = 30 - birth_date
elif(m3 == 28):
    n1 = 28 - birth_date
elif (m3 == 29):
    n1 = 29 - birth_date
b2 =0
if(today_month < birth_month):
    today_date -=1
else:
    b2 = 1

non_leap_year_count = ((today_year) - (birth_year+b2 )) - leap_year_count

no_of_days_in_year = (non_leap_year_count * 365) + (leap_year_count * 366)

days = no_of_days_in_year + m1 + m2 +  today_date + n1

print("or", (int(year_count) * 12 + int(month_count)),"months and",today_date , "days old " )

print("or",int(days / 7),"weeks and",(days % 7),"days old" )
print("or " , days , " days old")
print("or",days * 24 , "Hours")
print("or",days *60 ,"minutes")
print("or",days *60*60 ,"seconds")

