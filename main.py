''' 
Installed 2 package(s) with pip: Matplotlib, Pandas
1 - Matplotlib: to plot and see the graph of the data
2 - Pandas: to read the data from the csv file and manipulate it
''' 

import pandas as pd                                                             # read data from the csv 
import csv
from datetime import datetime                                                   # manipulate date and time
from data_input import get_date, get_amount, get_category, get_description      # import the functions from data_input.py

class CSV:
    CSV_FILE = 'data.csv'                                               # class variable
    COLUMNS = ['Date', 'Amount', 'Category', 'Description']             # class variable

    @classmethod
    def initialize_csv(cls):                                            # class method - initialize csv
        try:
            pd.read_csv(cls.CSV_FILE)                                   # exist - read 
        except FileNotFoundError:                                       # not exist - create one 
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_data(cls, date, amount, category, description):             # class method - add data to csv 
        new_data = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        with open(cls.CSV_FILE, mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_data)
        print("Data added successfully")

CSV.initialize_csv()                                                        # initialize the csv file
#CSV.add_data('01-01-2024', 1000, 'Income', 'Salary')                       # manual check add data 