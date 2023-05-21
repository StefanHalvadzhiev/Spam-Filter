import nltk
from nltk.corpus import stopwords
import pandas as pd


nltk.download("stopwords")


def reomve_stop_words(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_keep = df.columns.difference(stopwords.words("english"))
    return df[columns_to_keep]
