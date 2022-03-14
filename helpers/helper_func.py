import pandas as pd


def get_category(df: pd.DataFrame) -> pd.DataFrame:
    """Assigns a category based on week of the year and brand_id.

    Args:
        df (pd.DataFrame)

    Returns:
        pd.DataFrame: Updated dataframe with new category column.
    """
    x = df.copy()

    x['created_at'] = pd.to_datetime(df['created_at'])

    x['category'] = x[['created_at', 'brand_id']].apply(
        lambda row: f"Week_{row.created_at.week}_{row.brand_id}",
        axis=1)

    x['created_at'] = df['created_at'].astype(str)
    return x


def create_google_sheet(df: pd.DataFrame, sheet) -> None:
    """Assigns records based on their category (week of the year and brand_id) to worksheets.

    Args:
        df (pd.DataFrame)
        sheet (spreadsheet of google sheets):

    Returns:
        None
    """
    for category in df['category'].unique():
        new_df = df[df['category'] == category]
        worksheet = sheet.add_worksheet(title=category, rows=new_df.shape[0], cols=len(new_df.columns))
        worksheet.update([new_df.columns.values.tolist()] + new_df.values.tolist())
