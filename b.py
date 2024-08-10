import numpy as np
with open("Day2ex2.csv", "r") as f:
	f = f.readlines()
	f = list(map(float, f[0].split(",")))
print((16 - np.mean(f)) /  (np.std(f) ** 0.5 / (30 ** 0.5)))