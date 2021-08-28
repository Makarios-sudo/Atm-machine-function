#prompt = int(input("""
#"""))
#banks = {'1': "first bank","2": "access bank", "3": "zenith","4": "gtbank"}

# for value in banks.values():
# print(value)
select_bank = int(input("""
        select bank
. ......
1. first bank               8.  fidelity
2. access/diamond bank      9.  stanbic
3  zenith                   10. union
4. uba                      11. wema
5. ecobank                  12. providus
6. polaris bank             13  citi
7. fcmb

>>>: """))

banks = (
'', 'first bank', 'access/diamond bank', 'zenith bank', "uba", 'ecobank', "polaris bank", 'fcmb', 'fidelity',
'stanbic', 'union bank', 'wema bank', 'providus', 'citi')

print(banks[select_bank])


