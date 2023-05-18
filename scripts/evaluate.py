def evaluate(number1: str, number2: str) -> None:
    print(
        f"Number of mislabeled points out of a total {number1} points : {number2}"
    )
    print(f"Accuracy of Gaussian model: {100 - number2 / number1 * 100}")
