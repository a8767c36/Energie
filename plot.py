import matplotlib.pyplot as plt
import numpy as np

years = [ 2020,  2025,  2030,  2035,  2040,   2045,   2050]
# in TWh
solar = [  854,  2500,  8540, 25000, 85400, 120000, 120000]
wind  = [ 1594,  3744, 10076, 27199, 60000,  60000,  60000]
water = [ 4359,  4359,  4359,  3000,  2000,   1500,   1000]
plant = [12185, 12185, 12185, 12185, 12185,  20000,  20000]
gas   = [38603, 38603, 38603, 38603, 13500,      0,      0]
oil   = [48610, 48610, 48610, 48610, 13500,      0,      0]
coal  = [42233, 42233, 42233, 42233, 13500,      0,      0]

gsmt = [146000,150000,162000,195000,200000, 200000, 200000]

nclr  = [ 2679,  2679,  2679,  2679,  1300,      0,      0]

plt.title("World Energy outlook '2050")
plt.stackplot(years,
	[
		coal, oil, gas,
		plant,
		water, wind, solar,
	],
	colors = (
		"#533", "#733", "#933",
		"#3b3",
		"#3bb", "#33b", "#11f",
	),
	labels = (
		"Coal", "Oil", "Gas",
		"Renewable Biomass",
		"Water power", "Wind", "Solar"
	)
)
plt.legend()
#plt.show()
plt.savefig("plot.png", dpi=400)
