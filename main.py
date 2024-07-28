''' 
Installed 2 package(s) with pip: Matplotlib, Pandas
1 - Matplotlib: to plot and see the graph of the data
2 - Pandas: to read the data from the csv file and manipulate it
''' 

import pandas as pd                                                     # Allow to read the data from the csv file
import csv
from datetime import datetime                                           # Allow to manipulate the date and time

class CSV:
    CSV_FILE = 'data.csv'                                               # class variable
    COLUMNS = ['Date', 'Amount', 'Category', 'Description']             # class variable

    @classmethod                                                        # access only to class and not to its instance
    def initialize_csv(cls):                                            # class method to initialize the csv file
        try:
            pd.read_csv(cls.CSV_FILE)                                   # if exist, read the csv file
        except FileNotFoundError:                                       # create one if it doesn't exist
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_data(cls, date, amount, category, description):             # class method to add data to the csv file
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

CSV.initialize_csv()                                                    # call the class method to initialize the csv file
CSV.add_data('01-01-2024', 1000, 'Income', 'Salary')                        # call the class method to add data to the csv file