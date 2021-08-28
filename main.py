

"""writing code on the functioning of an Atm machine """

default_pin = 1234
pin_limit = 3
enter_pin = 1

name = input("enter your name \n>>> ".title())
print(f"\nhello {name},".title())

while enter_pin <= pin_limit:

    pin = int(input(f"your default pin is 1234\n\nplease enter your default pin \n>>> ".title()))
    enter_pin += 1

    if default_pin == pin:
        transaction = int(input("""
        how can we help you
        

1. check balance       4. change pin
2. withdraw            5. pay bills
3. transfer            6. request for atm card

0. cancelled transaction
>>>  """.title()))

        if transaction == 0:
            print('you request is been cancelled')
            break

        elif transaction == 1:

            savings_account = 100000
            current_account = 100000

            balance = int(input("""
    enter the account type
1. savings          2. current
>>> """.title()))
            if balance == 1:
                print(f"your savings account is {savings_account} dollars")

            elif balance == 2:
                print(f"your savings account is {current_account} dollars")

            else:
                print("wrong input")

        elif transaction == 2:
            """ making a code for withdrawal """

            savings_account = 100000
            current_account = 100000
            withdrawal = 0

            account_type = int(input("""
    enter the account type
1. savings          2. current
>>> """.title()))

            if account_type == 1:
                prompt = int(input("\nenter amount\n>>> ".title()))

                if prompt <= savings_account:
                    print(f"your withdrawal of {prompt}dollars is successful".title())

                elif prompt > savings_account:
                    print("\ninsufficient funds, please fund your account".title())

            elif account_type == 2:

                prompt = int(input("\nenter amount\n>>> ".title()))

                if prompt <= current_account:
                    print(f"your withdrawal {prompt}dollars is successful".title())

                elif prompt > current_account:
                    print("\ninsufficient funds, please fund your account".title())

            else:
                print("error, wrong input")

        elif transaction == 3:
            amount = int(input("enter amount \n>>> ".title()))

            select_bank = int(input("""
           select bank
........................................
1. first bank               8.  fidelity
2. access/diamond bank      9.  stanbic
3  zenith                   10. union
4. uba                      11. wema
5. ecobank                  12. providus
6. polaris bank             13. citi
7. fcmb                     14. gtbank

>>>: """.title()))

            banks = (
                '', 'first bank', 'access/diamond bank', 'zenith bank', "uba", 'ecobank', "polaris bank", 'fcmb',
                'fidelity', 'stanbic', 'union bank', 'wema bank', 'providus', 'citi')

            if amount <= 100000:
                print(f"\nyour transfer of {amount} to {banks[select_bank]} is successful")
            else:
                print("\ninsufficient fund")

        elif transaction == 4:

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
                    break

            else:
                print("you have exceed the limit, please try again in 2 hours time".title())
            break

        elif transaction == 5:

            bills = ['', 'phcn', 'lasma', 'dstv/gotv', 'utility', 'tax']

            banks = ('', 'first bank', 'access/diamond bank', 'zenith bank', "uba", 'ecobank', "polaris bank", 'fcmb',
                     'fidelity','stanbic', 'union bank', 'wema bank', 'providus', 'citi', 'gtbank')

            prompt = int(input("""
select bills

1. phcn         4. utility
2. lasma        5. tax
3. dstv/gotv

>>> """.upper()))

            amount = int(input(f"\nenter amount of {bills[prompt]} bill\n>>> ".title()))
            account = int(input("\nenter the account number\n>>> ".title()))
            select_bank = int(input("""
        select bank
..........................................
1. first bank               8.  fidelity
2. access/diamond bank      9.  stanbic
3  zenith                   10. union
4. uba                      11. wema
5. ecobank                  12. providus
6. polaris bank             13  citi
7. fcmb                     14. gtbank

>>>: """.title()))
            if amount <= 10000:
                print(f"\nyour payment of {amount} to {banks[select_bank]} for {bills[prompt]} bill is successful".title())
            else:
                print('insufficient funds')
            break

        elif transaction == 6:
            name = input("please enter your name\n>>> ")
            acc_number = int(input("please enter your account number\n>>> "))
            print("your ATM card will be ready in the next 2 day, thank you")
            print("for any complaint, please call our customer service on +234-8138881777")
            break

    else:
        print("wrong pin, try again ")

else:
    print('\nthank you for banking with us'.title())

