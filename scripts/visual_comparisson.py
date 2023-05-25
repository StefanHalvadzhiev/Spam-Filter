from typing import Dict

import matplotlib.pyplot as plt


def create_barplots(data_dict: Dict[str, float]) -> None:
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(keys, values, color="steelblue", hatch="//")

    # Display numeric values above each bar
    for i, value in enumerate(values):
        ax.text(i, value, str(value), ha="center", va="bottom")

    ax.set_xlabel("Keys")
    ax.set_ylabel("Values")
    ax.set_title("Bar Plots")

    plt.show()
