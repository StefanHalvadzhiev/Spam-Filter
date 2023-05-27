def evaluate(number1: str, number2: str, calculation_type: str) -> float:
    print(
        f"Number of mislabeled points out of a total {number1} points : {number2}"
    )
    percentage = 100 - number2 / number1 * 100
    print(f"Accuracy of {calculation_type} model: {percentage}")
    return percentage
