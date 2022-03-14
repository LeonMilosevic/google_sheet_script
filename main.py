import gspread
from helpers.helper_func import get_category, create_google_sheet
import pandas as pd


def app():
    gs_file_name = "cc_task_2"
    sa = gspread.service_account()
    sheet = sa.open(gs_file_name)

    df = pd.read_csv("./source/grouped_tickets")

    df = get_category(df)

    df = df.fillna('NaN')

    create_google_sheet(df, sheet)


if __name__ == '__main__':
    app()
