import  csv
import sqlite3
import pandas as pd
import db_actions
def generate_report():
    with open(r'D:\ula\studia\sem6\IoT\Lab5\report.csv', 'w+') as write_file:
    # open a file to write to
        conn = sqlite3.connect(r'D:\ula\studia\sem6\IoT\Lab5\taskDB.db')
        # connect to your database
        cursor = conn.cursor()
        # create a cursor object (which lets you address the table results individually)
        for row in cursor.execute('SELECT * FROM data_logs'):
        # use the cursor as an iterable
            write_file.write(row)
            # write to the csv, then you can open the csv in Excel.
            # Open up your csv in Excel.
    # You can also use the 'csv' module, which has an Excel dialect.