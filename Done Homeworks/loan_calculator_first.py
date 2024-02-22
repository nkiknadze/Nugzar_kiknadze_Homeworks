'''
სესხის კალკულატორი, რომელმაც უნდა და დაითვალოს შემდეგი მონაცემების მიხედვით სესხზე ყოველთვიური გადასახდელი თანხა.
 - სესხის მოცულობა
 - წლიური საპროცენტო განაკვეთი
 - სესხის ვადა (წელი, თვე)

პროგრამა უნდა თხოვდეს "კლიენტი"-ს შესახებ ზოგად ინფორმაციას და საბოლოოდ დაგენერირებული მონაცმეების 
ამოღება უნდა EXCEL ან PDF ფორმატში, მცირე განაცხადის ფორმატით.

საბეჭდ ფორმაშ უნდა ამოდიოდეს დაგენერირებსი თარიღი.

თუ შევძელი ეროვნული ბანკის გაცვლითი კურსის საიტიდან წამოღება, მაშინ ვალუტაში გაკეთებულ სესხზე
უნდა ახდენდეს კურსის გამრავლებას 

'''
# მოდულების იმპორტი
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate
from io import BytesIO
from openpyxl import Workbook

# კალკულატორის ძრითადი კლასი
class LoanCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # ინტერფეისისთვის და ველების შექმნა, რომლებსაც გადაეცემათ ფუნქციები
    def initUI(self):
        self.setWindowTitle('Loan calculator')
        self.setGeometry(300, 300, 600, 400)
        self.setupInputFields()
        self.setupCalculateButton()
        self.setupResultTable()
        self.setupExportButton()

    def setupInputFields(self):
        layout = QFormLayout(self)
        self.setLayout(layout)

        self.loan_amount_edit = QLineEdit()
        layout.addRow('Loan Amount:', self.loan_amount_edit)

        self.interest_rate_edit = QLineEdit()
        layout.addRow('Interest rate (%):', self.interest_rate_edit)

        self.loan_term_years_edit = QLineEdit()
        layout.addRow('Term (Years):', self.loan_term_years_edit)

        self.loan_term_months_edit = QLineEdit()
        layout.addRow('Term (Months):', self.loan_term_months_edit)

    # კალკულაციის ღილაკის ფუნქცია, რომელსაც გადაეცემა, კალკულაციის ფუნქცია
    def setupCalculateButton(self):
        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_payment)
        self.layout().addWidget(self.calculate_button)

    # დაგენერირებული შედეგის გამოტანა
    def setupResultTable(self):
        self.result_table = QTableWidget()
        self.result_table.setColumnCount(5)
        self.result_table.setHorizontalHeaderLabels(["Payment #", "Payment Date", "Payment Amount", "Interest", "Principal"])
        self.layout().addWidget(self.result_table)

    # Excel-ში ექსპოტის ფუქნცია
    def setupExportButton(self):
        self.export_button = QPushButton('Export to Excel')
        self.export_button.clicked.connect(self.export_to_excel)
        self.layout().addWidget(self.export_button)

    # ყოველთვიური გადახდების კალკულაციის ფუნქცია
    def calculate_payment(self):
        try:
            # მომხმარებლის მიერ შემოყვანილი ინფორმაიცის მიღება და დაანგარიშება
            loan_amount = float(self.loan_amount_edit.text())
            interest_rate = float(self.interest_rate_edit.text()) / 100
            loan_term_years = int(self.loan_term_years_edit.text())
            loan_term_months = int(self.loan_term_months_edit.text()) if self.loan_term_months_edit.text() else 0
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter valid numbers for loan amount, interest rate, and loan term.')
            return


        total_loan_term_months = loan_term_years * 12 + loan_term_months
        monthly_payment = self.calculate_monthly_payment(loan_amount, interest_rate, total_loan_term_months)
        self.populate_result_table(monthly_payment, total_loan_term_months)

    def calculate_monthly_payment(self, loan_amount, interest_rate, total_loan_term_months):
        monthly_interest_rate = interest_rate / 12
        n = total_loan_term_months
        payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -n)
        return payment

    # მირებული შედეგის მიხედვით ცხრილსი შევსება
    def populate_result_table(self, monthly_payment, total_loan_term_months):
        self.result_table.setRowCount(total_loan_term_months + 1)

        loan_issue_date = QDate.currentDate()
        first_payment_date = loan_issue_date.addDays(30)

        remaining_loan_amount = float(self.loan_amount_edit.text())
        total_interest = 0
        total_principal = 0
        for payment_num in range(total_loan_term_months):
            interest_payment = remaining_loan_amount * (float(self.interest_rate_edit.text()) / 100) / 12
            principal_payment = monthly_payment - interest_payment
            remaining_loan_amount -= principal_payment

            payment_date = first_payment_date.addMonths(payment_num)
            self.result_table.setItem(payment_num, 0, QTableWidgetItem(str(payment_num + 1)))
            self.result_table.setItem(payment_num, 1, QTableWidgetItem(payment_date.toString('yyyy-MM-dd')))
            self.result_table.setItem(payment_num, 2, QTableWidgetItem(f"${monthly_payment:.2f}"))
            self.result_table.setItem(payment_num, 3, QTableWidgetItem(f"${interest_payment:.2f}"))
            self.result_table.setItem(payment_num, 4, QTableWidgetItem(f"${principal_payment:.2f}"))
            total_interest += interest_payment
            total_principal += principal_payment

        # ყოველთვიური გადასახდელების მიხედვით ჯამური თანხის გამოტანა (ჯამური პროცენტი და ჯამური ძირითადი თანხა)
        self.result_table.setItem(total_loan_term_months, 0, QTableWidgetItem('Total'))
        self.result_table.setItem(total_loan_term_months, 3, QTableWidgetItem(f"${total_interest:.2f}"))
        self.result_table.setItem(total_loan_term_months, 4, QTableWidgetItem(f"${total_principal:.2f}"))

    # ექსელში დაგენერირება. 
    def export_to_excel(self):
        df = []
        headers = [self.result_table.horizontalHeaderItem(col).text() for col in range(self.result_table.columnCount())]
        df.append(headers)

        for row in range(self.result_table.rowCount() - 1):
            row_data = [self.result_table.item(row, col).text() for col in range(self.result_table.columnCount())]
            df.append(row_data)

        total_row = ['Total', '', '', '']
        total_interest = 0
        total_principal = 0
        for row in range(1, len(df)):
            total_interest += float(df[row][3][1:])
            total_principal += float(df[row][4][1:])
        total_row.append(f"${total_interest:.2f}")
        total_row.append(f"${total_principal:.2f}")
        df.append(total_row)

        wb = Workbook()
        ws = wb.active
        for r_idx, row in enumerate(df, 1):
            for c_idx, value in enumerate(row, 1):
                if c_idx == 2:
                    value = value.replace('/', '-')
                ws.cell(row=r_idx, column=c_idx, value=value)

        buffer = BytesIO()
        wb.save(buffer)

        try:
            # ფაილისთვის უნიკალური სახელის დარქმევა და დაგენერირება
            filename = f'Loan_schedule_{len(os.listdir()) // 2 + 1}.xlsx'
            with open(filename, 'wb') as f:
                f.write(buffer.getvalue())
            QMessageBox.information(self, 'ok', 'Excel file generated successfully!')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to generate Excel file: {str(e)}')

# ძირითადი ფუნქციის გამოძახება
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoanCalculator()
    window.show()
    sys.exit(app.exec_())
