from modules.loan import Loan


class main:
    while True:
        print('Pasirinkite veiksmą: \n'
              '1. Įvesti duomenys. '
              '2. Parodyti informaciją. '
              '3. Parodyti mokėjimo grafiką. '
              '4. Baigti darbą.\n')
        action = input()

        if action == '1':
            loan_sum = input('Paskolos suma: ')
            term = input('Paskolos terminas mėn.: ')
            interest = input('Paskolos palūkanos %: ')
            loan = Loan(loan_sum, term, interest)

            print('\nPaskolos objektas sukurtas!\n')

        elif action == '2':

            try:
                loan.loan_info()
            except:
                print('Pirmą įveskite duomenys!\n')

        elif action == '3':
            try:
                loan.payment_schedule()
            except:
                print('Pirmą įveskite duomenys!\n')

        elif action == '4':
            break

        else:
            print('Blogai pasirinktas veiksmas, pasirinkite iš naujo!\n')
            continue
