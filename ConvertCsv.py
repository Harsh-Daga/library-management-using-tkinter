from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import pandas as pd
import csv
import sys




mypass = "Root1234@"
mydatabase="library"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def convertCsv():
    sql = 'SELECT * from books;'
    csv_file_path = 'List_of_Books.csv'

    try:
        cur.execute(sql)
        rows = cur.fetchall()
    finally:
        con.close()

    # Continue only if there are rows returned.
    if rows:
        # New empty list called 'result'. This will be written to a file.
        result = list()

        # The row name is the first entry for each entity in the description tuple.
        column_names = list()
        for i in cur.description:
            column_names.append(i[0])

        result.append(column_names)
        for row in rows:
            result.append(row)

        # Write result to file.
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)
    else:
        sys.exit("No rows found for query: {}".format(sql))
