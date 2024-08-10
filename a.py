import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("day2ex1.csv")
print(np.mean(df["Class A"]))
plt.plot(sorted(df["Class A"]), df["Class A"].index)
plt.plot(sorted(df["Class B"]), df["Class B"].index)
plt.show()