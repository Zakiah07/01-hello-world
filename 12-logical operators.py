#use in a situation with multiple conditions, logical and operator, logical or operator
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit: #with logical operator or, either one statement must be true
    print("Eligible for loan")

if has_high_income and not has_good_credit:
    print("Eligible for loan")