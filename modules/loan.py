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
        'Suskaičiuoja ir parodo mokėjimo grafiką'
        loan_left = self.loan_sum
        loan_part = self.loan_sum / self.term

        print("{:>10}\t{:>10}\t{:>10}\t{:>10}\t{:>10}\t".format(
            'Mėnuo', 'Mėnesinė', 'Paskolos',
            'Mėnesio', 'Bendra'))
        print("{:>10}\t{:>10}\t{:>10}\t{:>10}\t{:>10}\t".format(
            '', 'paskolos', 'likutis',
            'palūkanos', 'mokėtina'))
        print("{:>10}\t{:>10}\t{:>10}\t{:>10}\t{:>10}\t".format(
            '', 'dalis', '',
            '', 'suma'))

        for month in range(self.term):
            monthly_interest = loan_left * self.interest / (12 * 100)
            loan_left -= loan_part
            monthly_sum = loan_part + monthly_interest
            print("{:>10}\t{:>10}\t{:>10}\t{:>10}\t{:>10}\t".format(
                month + 1, round(loan_part, 2), round(loan_left, 2),
                round(monthly_interest, 2), round(monthly_sum, 2)))

        print("{:>10}\t{:>10}\t{:>10}\t{:>10}\t{:>10}\t\n".format(
            'Iš viso', self.loan_sum, '',
            self.loan_calc()[0], self.loan_calc()[1]))
