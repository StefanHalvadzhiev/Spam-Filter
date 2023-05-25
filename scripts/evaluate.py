def evaluate(number1: str, number2: str) -> float:
    print(
        f"Number of mislabeled points out of a total {number1} points : {number2}"
    )
    percentage = 100 - number2 / number1 * 100
    print(f"Accuracy of Gaussian model: {percentage}")
    return percentage
