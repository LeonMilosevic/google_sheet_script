import gspread
from helpers.helper_func import get_category
import pandas as pd


# connect to spreadsheet google auth
# load csv

# approach #1
# read csv in gspread
# manipulate the csv using python to categorize data into weeks by year and brand_id
# example: wokrsheet: week_1, brand_id: 5000, week_1, brand_id: 4000...

# approach #2
# read csv using pandas
# manipulate the DF and categorize it into weeks by year and brand_id using pandas
# push it into spreadsheet google using gspread

def app():
    df = pd.read_csv("./source/grouped_tickets")
    
    df = get_category(df)


if __name__ == '__main__':
    app()
