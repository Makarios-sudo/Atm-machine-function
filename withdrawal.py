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
        print("your withdrawal is successful".title())

    elif prompt > savings_account:
        print("\ninsufficient funds".title())


elif account_type == 2:

    prompt = int(input("\nenter amount\n>>> ".title()))

    if prompt <= current_account:
        print("your withdrawal is successful".title())

    elif prompt > current_account:
        print("\ninsufficient funds".title())

else:
    print("error, wrong input")
