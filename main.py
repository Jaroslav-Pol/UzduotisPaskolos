from modules.loan import Loan

class main:
    while True:
        print('Pasirinkite veiksmą: '
              '1. Įvesti paskolos duomenys. '
              '2. Parodyti paskolos informaciją. '
              '3. Parodyti paskolos mokėjimo grafiką. '
              '4. Baigti darbą.  ')
        action = input()

        if action == '1':
            loan_sum = input('Paskolos suma: ')
            term = input('Paskolos terminas: ')
            interest = input('Paskolos palūkanos: ')
            loan = Loan(loan_sum, term, interest)

            print('\nPaskolos objektas sukurtas!\n')


        elif action == '2':
            loan.loan_info()

        elif action == '3':
            loan.payment_schedule()

        elif action == '4':
            break

        else:
            print('Blogai pasirinktas veiksmas, pasirinkite iš naujo!')
            continue

# nauja_paskola = Loan(2000, 12, 10)
# print(nauja_paskola.loan_info())
