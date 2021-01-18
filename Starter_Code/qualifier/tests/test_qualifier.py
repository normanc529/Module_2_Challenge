
import csv 

# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv(qualifying_loans, csv_output_path):
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

    csvpath_write = Path('./data/output/qualifying_loans.csv')        # this is the output path that i want to copy into the CLI file output path

    with open(csv_output_path, 'w', newline ='') as csvfile:
        
        header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
        
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)  #writes the header row in the csv file with the header list
        
        # for loan in qualifying_loans:
        #     #print(loan)                checks if loan(s) appear in the program so i can print it in the next line
        #     csvwriter.writerow(loan)





def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters(find_qualifying_loans):            #added find_qualifying_loans to argument of test_filters function
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!

# def run():
#     """The main function for running the script."""

#     # Load the latest Bank data
#     bank_data = load_bank_data()

#     # Get the applicant's information
#     credit_score, debt, income, loan_amount, home_value = get_applicant_info()

#     # Find qualifying loans
#     qualifying_loans = find_qualifying_loans(
#         bank_data, credit_score, debt, income, loan_amount, home_value
#     )

#     # Save qualifying loans
#     save_qualifying_loans(qualifying_loans)


# if __name__ == "__main__":
#     fire.Fire(run)
