""" changing the pin """


default_pin = 1234
trail = 1
while trail <= 3:
    default_pin = int(input("\nenter the default pin\n>>> ".title()))
    trail += 1

    if default_pin != 1234:
        print(f"wrong input".title())

    else:
        new_pin = int(input("\nenter your new pin\n>>> ".title()))
        confirm_pin = int(input("confirm new pin\n>>> ".title()))
        if new_pin == confirm_pin:
            new_pin = confirm_pin
            if confirm_pin == default_pin:
                print("\nyou new pin can not be the same with the default pin".title())
                break
            else:
                print(f"\nyour new pin is {confirm_pin}".title())
                break
        else:
            print("\nnew pin does not match confirmed pin, try again".title())

else:
    print("you have exceed the limit, please try again in 2 hours time".title())
