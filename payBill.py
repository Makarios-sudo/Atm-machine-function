""" CODES FOR Bill payment """

bills = ['', 'phcn', 'lasma', 'dstv/gotv', 'utility', 'tax']

banks = ('', 'first bank', 'access/diamond bank', 'zenith bank', "uba", 'ecobank', "polaris bank", 'fcmb', 'fidelity',
'stanbic', 'union bank', 'wema bank', 'providus', 'citi')


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
. ......
1. first bank               8.  fidelity
2. access/diamond bank      9.  stanbic
3  zenith                   10. union
4. uba                      11. wema
5. ecobank                  12. providus
6. polaris bank             13  citi
7. fcmb                     14. gtbank

>>>: """.title()))

print(f"\nyour payment of {amount} to {banks[select_bank]} for {bills[prompt]} bill is successful ")


