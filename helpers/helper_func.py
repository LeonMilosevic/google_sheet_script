import pandas as pd


def get_category(df: pd.DataFrame) -> pd.DataFrame:
    df['updated_at'] = pd.to_datetime(df['updated_at'])
    df['created_at'] = pd.to_datetime(df['created_at'])

    df['category'] = df[['created_at', 'brand_id']].apply(lambda row: f"Week_{row.created_at.week}_{row.brand_id}",
                                                          axis=1)

