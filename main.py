class Loan:
    def __init__(self, loan_sum, term, interest):
        self.loan_sum = int(loan_sum)
        self.term = int(term)
        self.interest = int(interest)
        # self.total_interest = self.loan_calc()


    def loan_info(self):

        print(f'Paskolos suma: {self.loan_sum}\nPaskolos terminas: {self.term}\n'
              f'Metinė palūkanų norma: {self.interest}%\n')

    def loan_calc(self):
        total_interest = round((self.loan_sum*self.interest/100*self.term)/12, 2)
        refund_sum = self.loan_sum + total_interest
        return total_interest
        # print(f'palukanos: {total_interest}\n Is viso {refund_sum}')


    def payment_schedule(self):
        pass



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
