# src/eda.py

import numpy as np
import matplotlib.pyplot as plt

def plot_price(df, save_path=None):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Price'])
    plt.title("Brent Oil Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    if save_path:
        plt.savefig(save_path)
    plt.show()


def add_log_returns(df):
    df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1))
    return df
