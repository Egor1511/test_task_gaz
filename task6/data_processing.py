from datetime import datetime

import pandas as pd


def json_to_dataframe(json_data: dict, column_mapping: dict) -> pd.DataFrame:
    """
    Converts JSON data to pandas.DataFrame and renames columns.

    Args:
    - json_data (dict): JSON data.
    - column_mapping (dict): Column mapping.

    Returns:
    - pandas.DataFrame: DataFrame with renamed columns.
    """
    df = pd.DataFrame(json_data["Rows"], columns=json_data["Columns"])
    df.rename(columns=column_mapping, inplace=True)
    return df


def add_load_datetime_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds load_dt column with current datetime.

    Args:
    - df (pandas.DataFrame): DataFrame.

    Returns:
    - pandas.DataFrame: DataFrame with load_dt column.
    """
    df["load_dt"] = datetime.now()
    return df
