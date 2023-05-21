from english_words import get_english_words_set
import pandas as pd


english_words_set = get_english_words_set(["web2"], lower=True)
columns_to_keep = None  # Initialize outside the function


def remove_non_english_words(df: pd.DataFrame) -> pd.DataFrame:
    global columns_to_keep  # Access the global variable

    if columns_to_keep is None:
        columns_to_keep = df.columns.intersection(english_words_set)

    df = df[["Prediction", "Email No."] + list(columns_to_keep)]
    return df
