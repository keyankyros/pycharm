def flames():
    your_name = input("enter your name: ")
    your_partner_name = input("enter your partner name: ")
    love_finder = "flames"
    list_1 = list(your_name)
    list_2 = list(your_partner_name)
    list_3 = list(love_finder)
    if(list_1 != list_2):
        for x in range(len(list_1)):
            if (list_1[x] == " "):
                list_1[x] = 0

            for y in range(len(list_2)):
                if (list_2[y] == " "):
                    list_2[y] = 0

                if (list_1[x] == list_2[y]):
                    list_1[x] = 0
                    list_2[y] = 0

        x = len(list_1) - list_1.count(0)
        y = len(list_2) - list_2.count(0)

        z = int(x + y)
        d = 5
        k = 0
        for a in range(1, len(list_3) * (z + 1)):
            if (len(list_3) == 1):
                break
            if (a % z == 0):
                list_3.pop(k)
                k -= 1
                d -= 1
            if (k == d):
                k = 0
            else:
                k += 1

        if (list_3[0] == 'f'):
            print(your_partner_name, " ", "is ", "friend ", "for you")
        elif (list_3[0] == 'l'):
            print(your_partner_name, " ", "is ", "lover ", "for you")
        elif (list_3[0] == 'a'):
            print(your_partner_name, " ", "is ", "affection ", "on you")
        elif (list_3[0] == 'm'):
            print(your_partner_name, " ", "is ", "marriage ", "with you")
        elif (list_3[0] == 'e'):
            print(your_partner_name, " ", "is ", "enemy ", "for you")
        elif (list_3[0] == 's'):
            print(your_partner_name, " ", "is ", "sister ", "for you")
    else:
        print("you and your partner name are same")



flames()
