import csv
import matplotlib.pyplot as plt
import numpy as np

# csv source
# https://ourworldindata.org/grapher/primary-energy-wind?tab=chart
# attention: all data is fake
# what the data says, is how much oil would be needed.
# however, we are interested in direct energy.
# so we have to multiply everything with 0.384.
csvfile = open('wind.csv', newline='')
rows = csv.reader(csvfile, delimiter = ',')
rows = [[int(r[2]), float(r[3])] for r in rows]

data = np.array(rows).T
# correcting the data format
for i in range(len(data[0])):
	data[1, i] = data[1, i] * 0.384
line = np.zeros(data.shape[1])
# regression line
# 1989:    3 ~ exp(1.100)
# 2022: 2107 ~ exp(7.653)
# year:      ~ exp(1.100 + 0.198 * (year-1989))
for i in range(len(line)):
	line[i] = np.exp(1.100 + 0.198 * (data[0, i] - 1989))

years = [2020, 2025, 2030, 2035, 2040, 2045, 2050]
print("predictions:")
for y in years:
	print(str(y), np.exp(1.100 + 0.198 * (y - 1989)))
print()

plt.title("primary energy (world: wind) in TWh")
plt.semilogy(data[0], data[1])
plt.semilogy(data[0], line)
plt.show()
