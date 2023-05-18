from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import (
    ComplementNB,
    BernoulliNB,
    MultinomialNB,
    GaussianNB,
)

import pandas as pd


def naive_bayes(type: str, dataset: pd.DataFrame):
    naive = None
    if type == "bernoully":
        naive = BernoulliNB()
    elif type == "complement":
        naive = ComplementNB()
    elif type == "multinomial":
        naive = MultinomialNB()
    elif type == "gaussian":
        naive = GaussianNB()

    X_train, X_test, y_train, y_test = train_test_split(
        dataset.drop(["Email No.", "Prediction"], axis=1),
        dataset["Prediction"],
    )

    y_pred = naive.fit(X_train, y_train).predict(X_test)

    test_size = X_test.shape[0]
    misleaded_size = (y_test != y_pred).sum()

    return test_size, misleaded_size
