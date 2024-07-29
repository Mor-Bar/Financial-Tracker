'''
All the functions related to getting the information from the user
for all the columns (date, amount, category, description)
'''

from datetime import datetime

date_format = '%d-%m-%Y'                        # for get_date function
CATEGORIES = {'I': 'Income', 'E': 'Expense'}    # for get_category function

def get_date(prompt, allow_default=False):
    date_str = input(prompt)                            
    if allow_default and not date_str:                                          # if the user just press enter - return today date
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)                   # check if the date format is correct - if so, return the date
        return valid_date.strftime(date_format)                      
    except ValueError:
        print("Invalid date format. Please enter in the format dd-mm-yyyy")
        return get_date(prompt, allow_default)                                  # if not, ask the user to enter again

def get_amount():
    try:
        amount = float(input("Enter the amount: "))                             # convert to float, else raise error
        if amount <= 0:
            raise ValueError("Amount cannot be negative or zero")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' - Income or 'E' - Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense")
    return get_category()

def get_description():
    return input("Enter the description (optional): ")