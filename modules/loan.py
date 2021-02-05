class Loan:
    def __init__(self, loan_sum, term, interest):
        self.loan_sum = int(loan_sum)
        self.term = int(term)
        self.interest = int(interest)
        # self.total_interest = self.loan_calc()

    def loan_info(self):
        'Atvaizduoja paskolos informaciją'

        print(f'Paskolos suma: {self.loan_sum} €.\n'
              f'Paskolos terminas: {self.term}mėn.\n'
              f'Metinė palūkanų norma: {self.interest}%\n'
              f'Palūkanų suma: {self.loan_calc()[0]} €\n'
              f'Bendra gražintina suma: {self.loan_calc()[1]} €')

    def loan_calc(self):
        'Gražina dvi reiksmes: palūkanų suma ir bendrą gražintiną sumą.'

        total_interest = round((self.loan_sum * self.interest / 100 * self.term) / 12, 2)
        refund_sum = self.loan_sum + total_interest
        return total_interest, refund_sum

    def payment_schedule(self):
        'Parodo mokėjimo grafiką'
        loan_left = self.loan_sum
        loan_part = round(self.loan_sum / self.term, 2)

        print("{:>6}\t{:>6}\t{:>6}\t{:>6}\t{:>6}\t".format(
            'Mėnuo', 'Gražintina paskolos dalis', 'Paskolos likutis',
            'Priskaičiuotos palūkanos', 'Bendra mokėtina suma'))

        for month in range(self.term):
            monthly_interest = round(loan_left * self.interest / (12 * 100), 2)
            loan_left -= loan_part
            monthly_sum = loan_part + monthly_interest
            print("{:>6}\t{:>6}\t{:>6}\t{:>6}\t{:>6}\t".format(
                month + 1, loan_part, loan_left, monthly_interest, monthly_sum))
